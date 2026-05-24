from backend.services.cache_manager import load_cache, save_cache
from backend.apis.fbref_scraper import scrape_player
import json


def update_fbref_data():

    cache = load_cache()

    try:
        with open("backend/data/fbref_links.json") as f:
            links = json.load(f)
    except:
        links = {}

    for name, url in links.items():

        print("Updating:", name)

        data = scrape_player(url)

        if data:
            cache[name] = data[:30]   # ✅ store last 30 matches only

    save_cache(cache)

    return {"status": "updated"}
``
