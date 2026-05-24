import requests, os

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_lineups(match_id):

    url = "https://sofasport.p.rapidapi.com/v1/events/lineups"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {"event_id": match_id}

    res = requests.get(url, headers=headers, params=params).json()

    players = []

    try:
        for team in res["data"]["lineups"]:
            for p in team["players"]:
                players.append({
                    "id": str(p["player"]["id"]),
                    "name": p["player"]["name"],
                    "position": p["player"]["position"]
                })
    except:
        return []

    return players
