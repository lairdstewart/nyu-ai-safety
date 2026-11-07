This repository serves as the static site https://nyuaisafety.org/ via Github
Pages and storage for club brand assets (e.g., SVG logos, HTML email templates).
The latter are stored in ./brand

# Website

engineering goals

- Mobile and desktop support
- Fast developer feedback (e.g., no or fast build)
- Fast to load/run (e.g., limit JS, large assets)
- Works on every major browser (Safari, Chrome, Firefox)

UI/UX goals

- Content-first
- Easy to navigate
- Non-pretentious

To test

- Run `npx serve` to run the site. This is necessary because the internal links
  don't specify ".html" on the end (to keep the final site links cleaner) but this
  breaks local file system navigation if not running on a server.

# Newsletter

## Sending a newsletter

newsletter/ contains html templates for the newsletter. To send a newsletter

1. Install Thunderbird, log into nyuaisafety@gmail.com account
2. Install mail merge plugin
3. Update email list with new entries from Airtable
4. Download email list as .csv
5. Make a copy of ./newsletter/weekly-bulletin-template-v2.html and Change local
   path of logo to absolute path (e.g.,
   file:///Users/foo/rectangle-white-purple-background.png)
6. Create a new email with {{Email}} in "To" field
7. Insert > HTML > select template
8. Draft the email by editing the template directly in Thunderbird. You can copy
   and paste headings/sections of the template
9. Click the mail merge button in the top right
10. Select Source: CSV > select the email list file
11. Keep Deliver Mode to "Send Later"
12. Click send, then confirm
13. In Local Folders > Outbox, confirm that the messages look correct
14. File --> send unsent messages

## Bulletin sources

- Slack
  - Blue dot opportunities channel

## calendar scraper

`newsletter/calendar-scrape.py` turns upcoming calendar events into a plain
text list.

1. Install [uv](https://docs.astral.sh/uv/)
2. `cd newsletter/`
3. `cp .env.example .env`
4. Set `ICAL_URLS` in `newsletter/.env` to a comma-separated list of iCal URLs
   (in Google Calendar: Settings → your calendar → "Public address in iCal
   format").
5. `uv init`
6. `uv run calendar-scrape.py`

This writes `newsletter/events.txt`.
