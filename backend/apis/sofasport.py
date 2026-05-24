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
        "date": date,
        "sport_id": "1",   # ✅ THIS FIXES YOUR ERROR
        "inverse": "false"
    }

    try:
        res = requests.get(url, headers=headers, params=params)

        if res.status_code != 200:
            return [{"error": f"API status {res.status_code}"}]

        data = res.json()

    except Exception as e:
        return [{"error": str(e)}]

    matches = []

    events = data.get("data", {}).get("events", [])

    if not events:
        return [{"status": "no matches found"}]

    for m in events:

        try:
            matches.append({
                "id": m.get("id"),
                "home": m.get("homeTeam", {}).get("name"),
                "away": m.get("awayTeam", {}).get("name"),
                "start": m.get("startTimestamp", 0)
            })
        except:
            continue

    return matches
