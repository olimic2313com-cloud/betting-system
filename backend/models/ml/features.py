import pandas as pd

def build_features(df):

    df = df.copy()

    # ✅ core features
    df["implied_prob"] = 1 / df["odds"]

    df["value_gap"] = df["prob"] - df["implied_prob"]

    df["log_odds"] = df["odds"].apply(lambda x: 0 if x <= 0 else x)

    # ✅ rolling hitrate (very important)
    df["hitrate_10"] = df["prob"].rolling(10, min_periods=1).mean()

    return df
