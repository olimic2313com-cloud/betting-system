
def get_fake_lineup():
    return [
        {"name": "Haaland", "position": "ST", "id": "1"},
        {"name": "Rodri", "position": "CDM", "id": "2"},
        {"name": "Maguire", "position": "CB", "id": "3"}
    ]

def calculate_base_prob(avg, line):
    return min(0.95, avg / (line + 1))


def run_engine():

    lineup = get_fake_lineup()
    bets = []

    for p in lineup:

        stats = {
            "shots": 2,
            "fouls": 1,
            "tackles": 2
        }

        STAT_LINES = {
            "shots": 1.5,
            "fouls": 1.5,
            "tackles": 1.5
        }

    for stat, line in STAT_LINES.items():

        avg = stats.get(stat, 0)

        base_prob = calculate_base_prob(avg, line)
        odds = 2.0

    # ✅ Use base model only (no ML)
        prob = base_prob

        edge = prob - (1 / odds)

        if prob > 0.6 and edge > 0.05:

            bets.append({
                "player": p["name"],
                "stat": stat,
                "line": line,
                "prob": round(prob, 2),
                "odds": odds,
                "edge": round(edge, 3),
                "reason": "Base model"
            })

    bets = sorted(bets, key=lambda x: x["edge"], reverse=True)
    return bets[:10]
