from fastapi import FastAPI
from backend.services.engine import run_engine

app = FastAPI()

@app.get("/")
def home():
    return {"status": "✅ backend working", "endpoint": "/bets"}

@app.get("/bets")
def bets():
    return run_engine()
