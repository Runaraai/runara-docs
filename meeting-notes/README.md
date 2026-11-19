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

Auth is keyless (Workload Identity Federation): no secret is stored in GitHub. The workflow federates into
Google Cloud project `main-entropy-495701-p6`, then uses the service account
`meeting-notes-sync@main-entropy-495701-p6.iam.gserviceaccount.com` with domain-wide delegation to read Drive.
Only this repo's `master` branch is allowed to do that.

Remaining setup (already done: project, service account, workload identity pool):

1. A Workspace super admin: Admin console → Security → Access and data control → API controls →
   **Manage Domain Wide Delegation** → add Client ID `111844503728521296630` with the single scope
   `https://www.googleapis.com/auth/drive.readonly`.
2. List the `@runara.ai` emails to scan in `scripts/meeting-notes-users.txt` and push.
3. Run the workflow once from the Actions tab to check it.

Gemini notes only exist for meetings where "Take notes for me" was on, and are owned by the organizer,
so list everyone who may organize meetings.

To keep a Drive doc out of the site (e.g. a test meeting), add its doc ID (the `source_id` in the note's header)
to `scripts/meeting-notes-ignore.txt` and delete the note file; the sync will skip it from then on.
