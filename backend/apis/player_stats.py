import requests, os

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_player_stats(player_id):

    url = "https://sofasport.p.rapidapi.com/v1/players/statistics/result"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "sofasport.p.rapidapi.com"
    }

    params = {
        "player_id": player_id,
        "player_stat_type": "overall"
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        data = res.json()

        stats = data.get("data", {})

        return {
            "shots": stats.get("shotsTotal", 0),
            "sot": stats.get("shotsOnTarget", 0)
        }

    except:
        return {"shots": 0, "sot": 0}
