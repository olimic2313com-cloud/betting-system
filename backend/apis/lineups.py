import requests
import os

API_KEY = os.getenv("RAPIDAPI_KEY")

CACHE = {}

def get_lineups(match_id):

    if match_id in CACHE:
        return CACHE[match_id]

    url = "https://sofasport.p.rapidapi.com/v1/events/lineups"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {"event_id": match_id}

    try:
        res = requests.get(url, headers=headers, params=params, timeout=3)
        data = res.json()
    except:
        return []

    players = []

    for team in data.get("data", {}).get("lineups", []):
        for p in team.get("players", []):
            players.append({
                "id": p["player"]["id"],
                "name": p["player"]["name"],
                "position": p["player"]["position"]
            })

    CACHE[match_id] = players

    return players
