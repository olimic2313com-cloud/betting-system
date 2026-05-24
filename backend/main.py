from fastapi import FastAPI, Query
from backend.services.engine import run_engine
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working ✅"}



@app.get("/bets")
def bets(date: str = None, games: int = 20):

    from datetime import datetime

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    return run_engine(date, games)
