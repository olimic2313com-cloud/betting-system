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
            "shots": int(row.get("Sh", 0)) if str(row.get("Sh")).isdigit() else 0,
            "sot": int(row.get("SoT", 0)) if str(row.get("SoT")).isdigit() else 0,
            "goals": int(row.get("Gls", 0)) if str(row.get("Gls")).isdigit() else 0,
            "assists": int(row.get("Ast", 0)) if str(row.get("Ast")).isdigit() else 0
        })

    return matches
