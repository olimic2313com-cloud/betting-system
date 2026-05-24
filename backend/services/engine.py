from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.apis.player_stats import get_player_stats

from backend.models.roles import get_role
from backend.models.position_zone import get_zone
from backend.models.matchup import matchup_boost
from backend.models.xg_model import calc_xg


def run_engine():

    try:
        matches = get_matches_by_date()
    except Exception as e:
        return [{"error": f"matches error: {str(e)}"}]

    if not matches or "error" in matches[0] or "status" in matches[0]:
        return matches

    bets = []

    for m in matches:

        try:
            players = get_lineups(m["id"])
        except Exception as e:
            return [{"error": f"lineups error: {str(e)}"}]

        if not players:
            continue

        for p in players:

            try:
                stats = get_player_stats(p["id"])
            except Exception:
                stats = {}

            shots = stats.get("shots", 0) if stats else 0
            sot = stats.get("sot", 0) if stats else 0

            try:
                role = get_role(p["position"])
                zone = get_zone(p["position"])
            except:
                role = "unknown"
                zone = "center"

            base_prob = min(0.95, shots / 2) if shots else 0.2
            xg = calc_xg(shots, sot)

            prob = base_prob * (1 + xg / 2)
            prob *= matchup_boost(p["position"], "CB")

            odds = 2.0
            edge = prob - (1 / odds)

            bets.append({
                "player": p.get("name", "unknown"),
                "team": m.get("home", "unknown"),
                "opponent": m.get("away", "unknown"),
                "prob": round(prob, 2),
                "xg": round(xg, 2),
                "edge": round(edge, 2),
                "role": role,
                "zone": zone,
                "shots": shots
            })

    if not bets:
        return [{"status": "no players or stats yet"}]

    return bets[:10]
``
