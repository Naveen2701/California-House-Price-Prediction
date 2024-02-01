import json
import requests


url = 'http://127.0.0.1:8000/house_price_prediction'

input_data_for_model = {
    
    'longitude' : -122.23,
    'latitude' : 37.88,
    'housing_median_age' : 35.0,
    'total_rooms' : 5.0,
    'total_bedrooms' : 2.0,
    'population' : 3.0,
    'households' : 4.0,
    'median_income' : 3.75,    
    'H_OCEAN' : 0,
    'INLAND' : 0,
    'ISLAND' : 0,
    'NEAR_BAY' : 1,
    'NEAR_OCEAN' : 1,
    'bedroom_ratio' : 0.8,
    'household_rooms' : 1.2
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print("The California House Price Prediction for given parameters is : " + "$ "+response.text)
