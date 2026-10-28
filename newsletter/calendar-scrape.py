import os
import urllib.request
from datetime import datetime, timedelta
from html import escape
from zoneinfo import ZoneInfo

import icalendar
import recurring_ical_events
from dotenv import load_dotenv

EST = ZoneInfo("America/New_York")


def to_datetime(value):
    if isinstance(value, datetime):
        return value.astimezone(EST)
    return datetime(value.year, value.month, value.day, tzinfo=EST)


def fmt_date(d):
    return d.strftime("%A, %B %-d")


def fmt_time(dt):
    return dt.strftime("%-I:%M %p")


def fmt_when(event):
    start = event.start
    end = event.end

    if not isinstance(start, datetime):
        last = end - timedelta(days=1) if end > start else start
        if last == start:
            return f"{fmt_date(start)} (all day)"
        return f"{fmt_date(start)} – {fmt_date(last)} (all day)"

    start = start.astimezone(EST)
    end = end.astimezone(EST)
    if start.date() == end.date():
        return f"{fmt_date(start)}, {fmt_time(start)} – {fmt_time(end)}"
    return f"{fmt_date(start)}, {fmt_time(start)} – {fmt_date(end)}, {fmt_time(end)}"


load_dotenv()
now = datetime.now(EST)
until = now + timedelta(days=30)

events: list[icalendar.Event] = []
for url in os.environ["ICAL_URLS"].split(","):
    calendar = icalendar.Calendar.from_ical(
        urllib.request.urlopen(url.strip()).read()
    )
    for event in recurring_ical_events.of(calendar).between(now, until):
        if not isinstance(event, icalendar.Event) or event.get("STATUS") == "CANCELLED":
            continue
        if now <= to_datetime(event.start) < until:
            events.append(event)

events.sort(key=lambda e: to_datetime(e.start))

parts = []
for event in events:
    title = escape(str(event.get("SUMMARY", "")))
    location = escape(str(event.get("LOCATION", "")))
    description = escape(" ".join(str(event.get("DESCRIPTION", "")).split()))
    parts.append(
        f"<h2>{title}</h2>\n"
        "<ul>\n"
        f"  <li>Time: {fmt_when(event)}</li>\n"
        f"  <li>Location: {location}</li>\n"
        f"  <li>Description: {description}</li>\n"
        "</ul>\n"
    )

with open("events.html", "w") as f:
    f.write("".join(parts))
