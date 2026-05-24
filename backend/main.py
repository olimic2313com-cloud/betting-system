from fastapi import FastAPI
from backend.services.engine import run_engine

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "✅ Backend running",
        "endpoint": "/bets"
    }


@app.get("/bets")
def get_bets():
    try:
        return run_engine()
    except Exception as e:
        return {"error": str(e)}
``
