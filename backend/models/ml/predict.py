import joblib
import pandas as pd

MODEL_FILE = "backend/models/ml/model.pkl"

def predict_prob(bet):

    try:
        model, features = joblib.load(MODEL_FILE)
    except:
        return bet["prob"]

    df = pd.DataFrame([bet])

    for f in features:
        if f not in df.columns:
            df[f] = 0

    X = df[features]

    prob = model.predict_proba(X)[0][1]

    return prob
