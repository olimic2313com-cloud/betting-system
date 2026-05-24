import requests, os

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_lineups(match_id):

    url = "https://sofasport.p.rapidapi.com/v1/events/lineups"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {"event_id": match_id}

    try:
        res = requests.get(url, headers=headers, params=params, timeout=5)
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

    return players
