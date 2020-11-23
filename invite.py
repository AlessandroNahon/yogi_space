from __future__ import print_function
import datetime
import random
from auth import auth
from playlist import playlist
from googleapiclient.discovery import build


def main():
    creds = None
    now = datetime.datetime.utcnow()
    oneHour = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    # If there are no (valid) credentials available, let the user log in.
    creds = auth(creds)

    vibes = playlist(creds)

    cal = build("calendar", "v3", credentials=creds)

    data = {
        "summary": "Yoga Time!",
        "location": "20 Gladstone Ave. Toronto Ontario M6J 3K6",
        "description": "Vibe out to some sweet sweet yoga, " + random.choice(vibes),
        "start": {
            "dateTime": now.isoformat("T") + "Z",
            "timeZone": "America/Toronto",
        },
        "end": {
            "dateTime": oneHour.isoformat("T") + "Z",
            "timeZone": "America/Toronto",
        },
        "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"],
        "attendees": [
            {"email": "alessandronahon@gmail.com"},
        ],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ],
        },
    }

    # Call the Calendar API
    event = cal.events().insert(calendarId="primary", body=data).execute()
    print("Event created: %s" % (event.get("htmlLink")))


if __name__ == "__main__":
    main()
