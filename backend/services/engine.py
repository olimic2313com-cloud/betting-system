from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.services.cache_manager import load_cache


def run_engine(date, games=20):

    matches = get_matches_by_date(date)

    # ✅ HANDLE ERROR (dict)
    if isinstance(matches, dict):
        return matches

    # ✅ HANDLE EMPTY
    if not matches:
        return {"status": "no matches"}

    cache = load_cache()

    result = []

    for m in matches:

        # ✅ Ensure it's actually a dict
        if not isinstance(m, dict):
            continue

        match_data = {
            "home": m.get("home"),
            "away": m.get("away"),
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

        for p in players[:5]:

            name = p.get("name")

            history = cache.get(name, [])

            if not isinstance(history, list):
                history = []

            vs_opponent = [
                g for g in history if isinstance(g, dict) and g.get("opponent") == m.get("away")
            ]

            match_data["players"].append({
                "name": name,
                "position": p.get("position"),
                "last_games": history[:games],
                "vs_opponent": vs_opponent[:5]
            })

        result.append(match_data)

    return result
