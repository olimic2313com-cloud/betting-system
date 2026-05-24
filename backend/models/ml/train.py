import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from backend.models.ml.features import build_features
from backend.models.ml.feature_select import select_features
import joblib

MODEL_FILE = "backend/models/ml/model.pkl"

def train():

    try:
        df = pd.read_csv("backend/tracker/bets.csv")
    except:
        print("No data yet")
        return

    # remove pending
    df = df[df["result"] != "pending"]

    if len(df) < 10:
        print("Not enough data")
        return

    df = build_features(df)

    df["target"] = (df["result"] == "win").astype(int)

    features = select_features(df)

    X = df[features]
    y = df["target"]

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )

    model.fit(X, y)

    joblib.dump((model, features), MODEL_FILE)

    print("✅ Model trained")
