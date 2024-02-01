from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json
import numpy as np


app = FastAPI()

class model_input(BaseModel):
    
    longitude : float
    latitude : float
    housing_median_age : float
    total_rooms : float
    total_bedrooms : float
    population : float
    households : float
    median_income : float    
    H_OCEAN : int
    INLAND : int
    ISLAND : int
    NEAR_BAY : int
    NEAR_OCEAN : int
    bedroom_ratio : float
    household_rooms : float
        
# loading the saved model
model = joblib.load('model.pkl')

@app.post('/house_price_prediction')
def model_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    lon = input_dictionary['longitude']
    lat = input_dictionary['latitude']
    age = input_dictionary['housing_median_age']
    room = input_dictionary['total_rooms']
    bed = input_dictionary['total_bedrooms']
    pop = input_dictionary['population']
    people = input_dictionary['households']
    income = input_dictionary['median_income']
    h_ocean = input_dictionary['H_OCEAN']
    inland = input_dictionary['INLAND']
    island = input_dictionary['ISLAND']
    near_bay = input_dictionary['NEAR_BAY']
    near_ocean = input_dictionary['NEAR_OCEAN']
    bed_rat = input_dictionary['bedroom_ratio']
    house_room = input_dictionary['household_rooms']
    
    input_list = [lon, lat, age, room, bed, pop, people, income, h_ocean, inland, island, near_bay, near_ocean, bed_rat, house_room]
    
    prediction = model.predict([input_list])
    return np.round(prediction[0])
    
    



