
import requests
import os

API_KEY = os.getenv("ODDS_API_KEY")

def get_odds():

    url = "https://api.the-odds-api.com/v4/sports/soccer/odds"

    params = {
        "apiKey": API_KEY,
        "regions": "eu",
        "markets": "player_shots"
    }

    res = requests.get(url, params=params).json()

    return res
