from backend.apis.sofasport import get_matches_by_date
from backend.apis.lineups import get_lineups
from backend.apis.player_stats import get_player_stats

from backend.models.roles import get_role
from backend.models.position_zone import get_zone
from backend.models.matchup import matchup_boost
from backend.models.xg_model import calc_xg


def run_engine():

    matches = get_matches_by_date()
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

            base_prob = min(0.95, shots / 2)

            xg = calc_xg(shots, sot)

            prob = base_prob * (1 + xg / 2)

            prob *= matchup_boost(p["position"], "CB")

            odds = 2.0
            edge = prob - (1 / odds)

            if prob > 0.6:

                bets.append({
                    "player": p["name"],
                    "team": m["home"],
                    "opponent": m["away"],
                    "prob": round(prob, 2),
                    "xg": round(xg, 2),
                    "edge": round(edge, 2),
                    "role": role,
                    "zone": zone
                })

    return bets[:10]

