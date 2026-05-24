from fastapi import FastAPI, Query
from backend.services.engine import run_engine
from backend.services.update_fbref import update_fbref_data

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/bets")
def bets(date: str, games: int = 20):
    return run_engine(date, games)


# ✅ trigger update manually
@app.get("/update")
def update():
    return update_fbref_data()
