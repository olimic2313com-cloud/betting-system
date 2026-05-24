import json

FILE = "backend/data/player_history.json"


def load_cache():

    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return {}


def save_cache(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
