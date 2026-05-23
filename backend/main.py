from fastapi import FastAPI
app = FastAPI()

@app.get("/bets")
def bets():
    return [
        {
            "player":"Bruno Fernandes",
            "team":"Man United",
            "opponent":"Chelsea",
            "prob":0.63,
            "odds":2.1,
            "hit_rate":19,
            "games":30,
            "image":"https://cdn.sofifa.net/players/206/517/23_120.png"
        }
    ]
