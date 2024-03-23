import requests
from datetime import datetime

APP_ID = "1cc74942"
API_KEY = "0992cc00251efd9ed15aebdc4af2c2a9"

GENDER = "male"
WEIGHT_KG = "69"
HEIGHT_CM = "170"
AGE = "19"

nuti_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/d0743d95537d5ce240b55b07f9d2d203/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nuti_endpoint, json=user_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%x")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": "Bearer YOUR_TOKEN"  # Replace YOUR_TOKEN with your actual token
    }
    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_input,
        headers=bearer_headers
    )

    print(sheet_response.text)
