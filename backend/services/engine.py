from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.services.cache_manager import load_cache


def run_engine(date, games=20):

    matches = get_matches_by_date(date)

    # ✅ Handle errors
    if isinstance(matches, dict):
        return matches

    if not matches:
        return {"status": "no matches"}

    cache = load_cache()

    result = []

    for m in matches:  # already limited in API

        match_data = {
            "home": m.get("home"),
            "away": m.get("away"),
            "league": m.get("league"),
            "players": []
        }

        try:
            players = get_lineups(m.get("id"))
        except:
            players = []

        if not players:
            match_data["status"] = "no lineups yet"
            result.append(match_data)
            continue

        for p in players[:5]:  # ✅ limit players

            name = p.get("name")
            history = cache.get(name, [])

            if not isinstance(history, list):
                history = []

            match_data["players"].append({
                "name": name,
                "position": p.get("position"),
                "last_games": history[:games]
            })

        result.append(match_data)

    return result
