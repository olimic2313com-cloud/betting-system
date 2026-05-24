
import json, os

FILE = "backend/data/team_defense.json"

def load():
    if os.path.exists(FILE):
        return json.load(open(FILE))
    return {}

def save(data):
    json.dump(data, open(FILE, "w"), indent=2)


def update_team_defense(team, is_home, shots_allowed):

    data = load()

    side = "home" if is_home else "away"

    if team not in data:
        data[team] = {"home": [], "away": []}

    data[team][side].append(shots_allowed)

    # keep last 20 matches
    data[team][side] = data[team][side][-20:]

    save(data)
