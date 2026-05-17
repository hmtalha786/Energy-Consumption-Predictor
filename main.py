# ==============================
# IMPORT LIBRARIES
# ==============================

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ==============================
# LOAD TRAINED MODEL
# ==============================

model = joblib.load("model/energy_model.pkl")

# ==============================
# CREATE FASTAPI APP
# ==============================

app = FastAPI()

# ==============================
# INPUT DATA SCHEMA
# ==============================

class EnergyInput(BaseModel):

    Square_Footage: float
    Number_of_Occupants: int
    Appliances_Used: int
    Average_Temperature: float
    Building_Type: str
    Day_of_Week: str

# ==============================
# HOME ROUTE
# ==============================

@app.get("/")
def home():
    return {"message": "Energy Prediction API Running"}

# ==============================
# PREDICTION ROUTE
# ==============================

@app.post("/predict")
def predict(data: EnergyInput):

    # Convert input into dataframe
    input_data = pd.DataFrame([{
        "Square Footage": data.Square_Footage,
        "Number of Occupants": data.Number_of_Occupants,
        "Appliances Used": data.Appliances_Used,
        "Average Temperature": data.Average_Temperature,
        "Building Type": data.Building_Type,
        "Day of Week": data.Day_of_Week
    }])

    # Predict
    prediction = model.predict(input_data)

    # Return prediction
    return {
        "Predicted Energy Consumption": round(float(prediction[0]), 2)
    }