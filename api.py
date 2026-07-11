from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
import joblib
import pandas as pd

app = FastAPI()

# load the model 
model = joblib.load('lgbm_model.pkl')
pipeline = joblib.load('pipeline.pkl')

class HouseFeatures(BaseModel):
    longitude:          float
    latitude:           float
    housing_median_age: float
    total_rooms:        float
    total_bedrooms:     float
    population:         float
    households:         float
    median_income:      float
    ocean_proximity:    str

@app.get('/')
def home():
    return {'message': 'California House Price Prediction'}

@app.post('/predict')
def predict(data: HouseFeatures):
    df = pd.DataFrame([data.model_dump()])

    df['rooms_per_household']      = df['total_rooms']    / df['households']
    df['bedrooms_per_room']        = df['total_bedrooms'] / df['total_rooms']
    df['population_per_household'] = df['population']     / df['households']

    prepared = pipeline.transform(df)
    prediction = model.predict(prepared)

    return {'prediction House Value': round(float(prediction[0]), 2)}