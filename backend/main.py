from fastapi import FastAPI, Query
from backend.services.engine import run_engine
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working ✅"}


@app.get("/bets")
def bets(date: str = None, games: int = 20):

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    try:
        return run_engine(date, games)
    except Exception as e:
        return {"error": str(e)}
