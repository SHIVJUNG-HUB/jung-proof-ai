import joblib

flood_model = joblib.load("backend/flood_model.pkl")
landslide_model = joblib.load("backend/landslide_model.pkl")

def risk_label(prob):
    if prob > 0.7:
        return "High"
    elif prob > 0.4:
        return "Medium"
    else:
        return "Low"

def predict_risk(data):
    flood_prob = flood_model.predict_proba(data)[0][1]
    landslide_prob = landslide_model.predict_proba(data)[0][1]

    return {
        "flood": (risk_label(flood_prob), flood_prob * 100),
        "landslide": (risk_label(landslide_prob), landslide_prob * 100)
    }
