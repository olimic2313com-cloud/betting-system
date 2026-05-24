from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.apis.player_stats import get_player_stats

from backend.models.roles import get_role
from backend.models.position_zone import get_zone
from backend.models.matchup import matchup_boost
from backend.models.xg_model import calc_xg


def run_engine():

    matches = get_matches_by_date()

    # ✅ HANDLE NO MATCHES
    if not matches or "error" in matches[0] or "status" in matches[0]:
        return matches

    bets = []

    for m in matches:

        players = get_lineups(m["id"])

        # ✅ HANDLE NO LINEUPS
        if not players:
            continue

        for p in players:

            stats = get_player_stats(p["id"])

            shots = stats.get("shots", 0) if stats else 0
            sot = stats.get("sot", 0) if stats else 0

            role = get_role(p["position"])
            zone = get_zone(p["position"])

            base_prob = min(0.95, shots / 2) if shots else 0.2

            xg = calc_xg(shots, sot)

            prob = base_prob * (1 + xg / 2)

            prob *= matchup_boost(p["position"], "CB")

            odds = 2.0
            edge = prob - (1 / odds)

            # ✅ SHOW PLAYERS EVEN IF LOW PROB (for testing)
            bets.append({
                "player": p["name"],
                "team": m["home"],
                "opponent": m["away"],
                "prob": round(prob, 2),
                "xg": round(xg, 2),
                "edge": round(edge, 2),
                "role": role,
                "zone": zone,
                "shots": shots
            })

    # ✅ HANDLE NO BETS
    if not bets:
        return [{"status": "no players with data yet (likely no lineups or stats)"}]

    return bets[:10]
