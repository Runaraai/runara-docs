# Meeting notes

One Markdown file per Google Meet meeting, named `YYYY-MM-DD-short-title.md`, starting with:

```
---
title: Weekly sync
date: 2026-11-18
attendees: Name, Name
---
```

After adding or editing notes run `python3 scripts/build-meeting-index.py` and commit `index.json` too.

## Automatic sync from Google Meet (Gemini notes)

`.github/workflows/sync-meeting-notes.yml` runs hourly (and on demand from the Actions tab). It runs
`scripts/sync_meeting_notes.py`, which copies new "Notes by Gemini" docs from Drive into this folder,
rebuilds `index.json` and commits. Notes already present (matched by `source_id`) are never overwritten.

One-time setup (needs a Google Workspace super admin):

1. In a Google Cloud project, enable the **Google Drive API**.
2. Create a service account (e.g. `meeting-notes-sync`) and a JSON key for it. Note its numeric **Client ID**.
3. Admin console → Security → Access and data control → API controls → **Manage Domain Wide Delegation** →
   add the Client ID with the single scope `https://www.googleapis.com/auth/drive.readonly`.
4. In this GitHub repo: Settings → Secrets and variables → Actions → new secret
   `GOOGLE_SERVICE_ACCOUNT_JSON` containing the whole key file.
5. List the `@runara.ai` emails to scan in `scripts/meeting-notes-users.txt`, push, then run the
   workflow once from the Actions tab.

Gemini notes only exist for meetings where "Take notes for me" was on, and are owned by the organizer,
so list everyone who may organize meetings.
