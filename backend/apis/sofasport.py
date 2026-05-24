import requests, os
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

    res = requests.get(url, headers=headers, params=params).json()

    matches = []

    for m in res.get("data", []):
        matches.append({
            "id": m["id"],
            "home": m["homeTeam"]["name"],
            "away": m["awayTeam"]["name"],
            "start": m["startTimestamp"]
        })

    return matches
