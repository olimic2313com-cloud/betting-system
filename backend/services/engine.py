from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.apis.player_stats import get_player_stats


def run_engine(date):

    matches = get_matches_by_date(date)

    # ✅ if API fails
    if not matches or "error" in matches[0]:
        return matches

    result = []

    for m in matches:

        match_data = {
            "home": m["home"],
            "away": m["away"],
            "league": m["league"],
            "players": []
        }

        players = get_lineups(m["id"])

        if not players:
            match_data["status"] = "no lineups yet"
            result.append(match_data)
            continue

        for p in players[:5]:   # ✅ limit for speed

            stats = get_player_stats(p["id"])

            match_data["players"].append({
                "name": p["name"],
                "position": p["position"],
                "shots": stats.get("shots", 0),
                "sot": stats.get("sot", 0)
            })

        result.append(match_data)

    return result
