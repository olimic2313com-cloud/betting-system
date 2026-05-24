def select_features(df):

    candidates = [
        "prob",
        "odds",
        "implied_prob",
        "value_gap",
        "hitrate_10"
    ]

    features = [f for f in candidates if f in df.columns]

    return features
