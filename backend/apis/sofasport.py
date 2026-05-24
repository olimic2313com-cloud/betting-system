import requests, os

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_live_matches():

    url = "https://sofasport.p.rapidapi.com/v1/events/schedule/live"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    res = requests.get(url, headers=headers).json()

    matches = []

    for m in res.get("data", []):
        matches.append({
            "id": m["id"],
            "home": m["homeTeam"]["name"],
            "away": m["awayTeam"]["name"]
        })

    return matches
``
