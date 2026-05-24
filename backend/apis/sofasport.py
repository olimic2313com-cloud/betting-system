import requests
import os
from datetime import datetime

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_matches_by_date(date=None):

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    url = "https://sofasport.p.rapidapi.com/v1/events/schedule/date"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {
        "date": date
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()
    except:
        return [{"error": "API request failed"}]

    matches = []

    # ✅ SAFE ACCESS (THIS IS THE FIX)
    events = data.get("data", {}).get("events", [])

    for m in events:

        try:
            matches.append({
                "id": m["id"],
                "home": m["homeTeam"]["name"],
                "away": m["awayTeam"]["name"],
                "start": m.get("startTimestamp", 0)
            })
        except:
            continue

    return matches
