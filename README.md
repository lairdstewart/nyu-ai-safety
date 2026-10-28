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

`newsletter/` holds a script that turns upcoming calendar events (the next 30
days, times shown in Eastern time) into plain HTML for the weekly newsletter.
Recurring events are expanded, and cancelled or modified occurrences are
respected.

Setup (requires [uv](https://docs.astral.sh/uv/)):

1. `cp newsletter/.env.example newsletter/.env`
2. Set `ICAL_URLS` in `newsletter/.env` to a comma-separated list of iCal URLs
   (in Google Calendar: Settings → your calendar → "Secret address in iCal
   format" or "Public address in iCal format").

Run:

```sh
cd newsletter
uv run main.py
```

This writes `newsletter/events.html`.
