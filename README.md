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

# Newsletter

## Sending a newsletter

newsletter/ contains html templates for the newsletter. To send a newsletter

1. Install Thunderbird
2. TODO write the rest of these instructions
3. Run the calendar scraper (instructions below) to gather events
4. Change local path to logo to absolute path (e.g., file:///Users/foo/rectangle-white-purple-background.png)

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
