import requests, os

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_matches_by_date(date):

    url = "https://sofasport.p.rapidapi.com/v1/events/schedule/date"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {
        "date": date,
        "sport_id": 1,
        "inverse": False
    }

    try:
        res = requests.get(url, headers=headers, params=params)

        if res.status_code != 200:
            return [{"error": f"status {res.status_code}"}]

        data = res.json()

    except Exception as e:
        return [{"error": str(e)}]

    matches = []

    events = data.get("data", {}).get("events", [])

    for m in events:
        matches.append({
            "id": m.get("id"),
            "home": m.get("homeTeam", {}).get("name"),
            "away": m.get("awayTeam", {}).get("name"),
            "league": m.get("tournament", {}).get("name"),
            "start": m.get("startTimestamp")
        })

    return matches
