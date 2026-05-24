from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.services.cache_manager import load_cache


def run_engine(date, games=20):

    matches = get_matches_by_date(date)

    if not matches or "error" in matches[0]:
        return matches

    cache = load_cache()

    result = []

    for m in matches:

        match_data = {
            "home": m["home"],
            "away": m["away"],
            "players": []
        }

        players = get_lineups(m["id"])

        if not players:
            match_data["status"] = "no lineups yet"
            result.append(match_data)
            continue

        for p in players:

            name = p["name"]

            history = cache.get(name, [])[:games]

            vs_opponent = [
                g for g in history if g["opponent"] == m["away"]
            ]

            match_data["players"].append({
                "name": name,
                "position": p["position"],
                "last_games": history,
                "vs_opponent": vs_opponent[:5]
            })

        result.append(match_data)

    return result
