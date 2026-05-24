from fastapi import FastAPI, Query
from backend.services.engine import run_engine

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working"}

@app.get("/bets")
def bets(date: str = Query(...)):
    return run_engine(date)
