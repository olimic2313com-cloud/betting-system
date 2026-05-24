import requests
import os

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_matches_by_date(date):

    url = "https://sofasport.p.rapidapi.com/v1/events/schedule/date"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {
        "date": str(date),
        "sport_id": "1",
        "inverse": "false"
    }

    try:
        res = requests.get(url, headers=headers, params=params, timeout=5)

        if res.status_code != 200:
            return {"error": f"status {res.status_code}"}

        data = res.json()

    except Exception as e:
        return {"error": str(e)}

    data_block = data.get("data")

    if isinstance(data_block, dict):
        events = data_block.get("events", [])
    elif isinstance(data_block, list):
        events = data_block
    else:
        events = []

    if not events:
        return {"status": "no matches found"}

    matches = []

    allowed_leagues = ["Premier League", "LaLiga"]

    for m in events:

        league = m.get("tournament", {}).get("name", "")

        if not any(l in league for l in allowed_leagues):
            continue

        matches.append({
            "id": m.get("id"),
            "home": m.get("homeTeam", {}).get("name"),
            "away": m.get("awayTeam", {}).get("name"),
            "league": league,
            "start": m.get("startTimestamp")
        })

    return matches[:5]  # ✅ LIMIT MATCHES

