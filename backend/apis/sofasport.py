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
        res = requests.get(url, headers=headers, params=params)

        if res.status_code != 200:
            return {
                "error": f"status {res.status_code}",
                "response": res.text
            }

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

    for m in events:
        matches.append({
            "id": m.get("id"),
            "home": m.get("homeTeam", {}).get("name"),
            "away": m.get("awayTeam", {}).get("name"),
            "league": m.get("tournament", {}).get("name"),
            "start": m.get("startTimestamp")
        })

    return matches
