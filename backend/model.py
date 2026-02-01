import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample training data
# [rainfall, river_level, soil_moisture, slope, crack, muddy, river_change, past_disaster]
X = np.array([
    [200,3,0.9,40,1,1,1,1],
    [150,2,0.8,35,1,0,1,1],
    [50,1,0.3,10,0,0,0,0],
    [80,1,0.4,15,0,0,0,0],
    [250,3,1.0,45,1,1,1,1],
    [120,2,0.6,25,0,1,0,1],
])

y_flood = [1,1,0,0,1,1]
y_landslide = [1,1,0,0,1,1]

flood_model = RandomForestClassifier()
landslide_model = RandomForestClassifier()

flood_model.fit(X, y_flood)
landslide_model.fit(X, y_landslide)

joblib.dump(flood_model, "backend/flood_model.pkl")
joblib.dump(landslide_model, "backend/landslide_model.pkl")

print("✅ Jung Proof AI models trained successfully")
