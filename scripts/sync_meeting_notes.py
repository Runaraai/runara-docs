#!/usr/bin/env python3
"""Copy Gemini meeting notes from Google Drive into meeting-notes/*.md.

For each user in scripts/meeting-notes-users.txt, impersonate them (service
account + domain-wide delegation, drive.readonly), find the "Notes by Gemini"
docs they OWN that changed recently, export each as Markdown and write it to
meeting-notes/ with a front-matter header. A note whose source_id is already
in the folder is skipped, so edits made in the repo are never overwritten.

Auth is keyless: GitHub Actions federates into Google (Workload Identity Federation) and the
resulting credentials call IAM signJwt on SERVICE_ACCOUNT_EMAIL to mint a domain-wide-delegation
token for each user.

Env: SERVICE_ACCOUNT_EMAIL, LOOKBACK_DAYS (default 3). Application Default Credentials must be set
(the workflow's google-github-actions/auth step does this).
"""
import datetime as dt
import base64
import json
import os
import pathlib
import re
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "meeting-notes"
USERS_FILE = pathlib.Path(__file__).resolve().parent / "meeting-notes-users.txt"
DOMAIN = "runara.ai"
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
API = "https://www.googleapis.com/drive/v3"
TITLE_RE = re.compile(r"^(?P<title>.*?)\s+-\s+(?P<y>\d{4})/(?P<m>\d{2})/(?P<d>\d{2})\b.*?-\s+Notes by Gemini\s*$")


def load_users():
    users = []
    for line in USERS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip().lower()
        if line:
            if not line.endswith("@" + DOMAIN):
                sys.exit(f"refusing non-{DOMAIN} user: {line}")
            users.append(line)
    return users


def parse_name(name, created):
    """('Weekly sync', '2026-11-18') from 'Weekly sync - 2026/11/18 10:00 GMT-08:00 - Notes by Gemini'."""
    m = TITLE_RE.match(name)
    if m:
        return m["title"].strip(), f"{m['y']}-{m['m']}-{m['d']}"
    return re.sub(r"\s*-\s*Notes by Gemini\s*$", "", name).strip() or name, created[:10]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "meeting"


def one_line(text):
    return re.sub(r"\s+", " ", text).strip()


IMG_RE = re.compile(r"^\[(image\d+)\]:\s*<data:image/(png|jpeg|jpg|gif|webp);base64,([A-Za-z0-9+/=\s]+)>[ \t]*$", re.M)
SURVEY_RE = re.compile(r"^\*Please \*\*rate the new Quick notes tab\*\*.*$\n?", re.M)


def clean_body(body, stem):
    """Drop Google's survey banner and move base64-embedded images out to meeting-notes/images/."""
    body = SURVEY_RE.sub("", body)

    def to_file(m):
        name, ext, data = m.group(1), m.group(2).replace("jpeg", "jpg"), m.group(3)
        img_dir = NOTES_DIR / "images"
        img_dir.mkdir(exist_ok=True)
        fname = f"{stem}-{name}.{ext}"
        (img_dir / fname).write_bytes(base64.b64decode(re.sub(r"\s+", "", data)))
        return f"[{name}]: meeting-notes/images/{fname}"

    return IMG_RE.sub(to_file, body)


def existing_source_ids():
    ids = set()
    for p in NOTES_DIR.glob("*.md"):
        m = re.search(r"^source_id:\s*(\S+)", p.read_text(encoding="utf-8")[:1000], re.M)
        if m:
            ids.add(m.group(1))
    return ids


def attendees_of(session, fid):
    r = session.get(f"{API}/files/{fid}", params={"fields": "permissions(emailAddress,displayName,role)"})
    if not r.ok:
        return ""
    out = []
    for p in r.json().get("permissions", []):
        email = p.get("emailAddress", "")
        if email.lower().endswith("@" + DOMAIN):
            out.append(one_line(p.get("displayName") or email))
    return ", ".join(sorted(set(out)))


def export_markdown(session, fid):
    for mime in ("text/markdown", "text/plain"):
        r = session.get(f"{API}/files/{fid}/export", params={"mimeType": mime})
        if r.ok:
            return r.text
    r.raise_for_status()


def user_session(adc, sa_email, user):
    """Requests session carrying a Drive token for `user`, via DWD, signed keylessly through IAM."""
    import requests
    now = int(time.time())
    payload = json.dumps({
        "iss": sa_email, "sub": user, "scope": " ".join(SCOPES),
        "aud": "https://oauth2.googleapis.com/token", "iat": now, "exp": now + 3600,
    })
    r = adc.post(f"https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/{sa_email}:signJwt",
                 json={"payload": payload})
    r.raise_for_status()
    t = requests.post("https://oauth2.googleapis.com/token", data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": r.json()["signedJwt"]})
    if not t.ok:
        raise RuntimeError(f"token exchange for {user} failed: {t.status_code} {t.text[:200]}")
    session = requests.Session()
    session.headers["Authorization"] = "Bearer " + t.json()["access_token"]
    return session


def main():
    import google.auth
    from google.auth.transport.requests import AuthorizedSession

    sa_email = os.environ.get("SERVICE_ACCOUNT_EMAIL")
    if not sa_email:
        print("::warning::SERVICE_ACCOUNT_EMAIL is not set; skipping sync")
        return
    adc_creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    from google.auth.transport.requests import Request
    adc_creds.refresh(Request())  # fails fast if the keyless federation is broken
    adc = AuthorizedSession(adc_creds)
    users = load_users()
    if not users:
        print("::warning::scripts/meeting-notes-users.txt has no users; nothing to scan")
        return
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=int(os.environ.get("LOOKBACK_DAYS", "3")))).strftime("%Y-%m-%dT%H:%M:%SZ")
    NOTES_DIR.mkdir(exist_ok=True)
    seen = existing_source_ids()
    added = 0
    for user in users:
        try:
            session = user_session(adc, sa_email, user)
        except Exception as e:
            print(f"::warning::{user}: {e}")
            continue
        q = ("mimeType='application/vnd.google-apps.document' and name contains 'Notes by Gemini' "
             f"and 'me' in owners and trashed=false and modifiedTime > '{since}'")
        page = None
        while True:
            params = {"q": q, "fields": "nextPageToken,files(id,name,createdTime)", "pageSize": 100}
            if page:
                params["pageToken"] = page
            r = session.get(f"{API}/files", params=params)
            if not r.ok:
                print(f"::warning::{user}: list failed {r.status_code} {r.text[:200]}")
                break
            data = r.json()
            for f in data.get("files", []):
                if f["id"] in seen:
                    continue
                title, date = parse_name(f["name"], f["createdTime"])
                body = export_markdown(session, f["id"])
                head = "\n".join([
                    "---",
                    f"title: {one_line(title)}",
                    f"date: {date}",
                    f"attendees: {attendees_of(session, f['id'])}",
                    f"source_id: {f['id']}",
                    "---",
                    "",
                ])
                path = NOTES_DIR / f"{date}-{slug(title)}.md"
                if path.exists():
                    path = NOTES_DIR / f"{date}-{slug(title)}-{f['id'][:6]}.md"
                body = clean_body(body, path.stem)
                path.write_text(head + body.strip() + "\n", encoding="utf-8")
                seen.add(f["id"])
                added += 1
                print(f"added {path.name}")
            page = data.get("nextPageToken")
            if not page:
                break
    print(f"{added} new note(s)")


if __name__ == "__main__":
    main()
