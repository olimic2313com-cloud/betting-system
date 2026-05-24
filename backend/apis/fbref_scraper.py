import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_player(url):

    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        table = soup.find("table")
        df = pd.read_html(str(table))[0]

    except:
        return []

    matches = []

    for _, row in df.iterrows():
        matches.append({
            "date": row.get("Date"),
            "opponent": row.get("Opponent"),
            "shots": row.get("Sh", 0),
            "sot": row.get("SoT", 0),
            "goals": row.get("Gls", 0),
            "assists": row.get("Ast", 0)
        })

    return matches
