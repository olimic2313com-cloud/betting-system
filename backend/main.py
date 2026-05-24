from fastapi import FastAPI
from backend.services.engine import run_engine

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "✅ Backend running",
        "endpoints": [
            "/run"
        ]
    }


@app.get("/run")
def run():
    try:
        bets = run_engine()
        return bets

    except Exception as e:
        return {
            "error": str(e)
        }
