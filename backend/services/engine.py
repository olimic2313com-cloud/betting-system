from backend.apis.sofasport import get_live_matches
from backend.apis.lineups import get_lineups
from backend.apis.player_stats import get_player_stats

from backend.models.roles import get_role
from backend.models.position_zone import get_zone
from backend.models.matchup import matchup_boost
from backend.models.xg_model import calc_xg


def run_engine():

    matches = get_live_matches()
    bets = []

    for m in matches:

        players = get_lineups(m["id"])

        for p in players:

            stats = get_player_stats(p["id"])

            if not stats:
                continue

            shots = stats.get("shots", 0)
            sot = stats.get("sot", 0)

            if shots == 0:
                continue

            role = get_role(p["position"])
            zone = get_zone(p["position"])

            # ✅ Base probability
            base_prob = min(0.95, shots / 2)

            # ✅ xG improvement
            xg = calc_xg(shots, sot)

            prob = base_prob * (1 + xg / 2)

            # ✅ simple matchup boost
            prob *= matchup_boost(p["position"], "CB")  # simplified

            odds = 2.0  # replace later
            edge = prob - (1 / odds)

            if prob > 0.6:

                bets.append({
                    "player": p["name"],
                    "team": m["home"],
                    "opponent": m["away"],
                    "stat": "shots",
                    "prob": round(prob, 2),
                    "xg": round(xg, 2),
                    "edge": round(edge, 2),
                    "role": role,
                    "zone": zone,
                    "reason": "real stats + xG + role"
                })

    return bets[:10]
