import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = os.environ.get("OWM_API_KEY") #YOUR APIKEY
account_sid = "AC2e1bd43835e9a0fcc63f4ab4849196be"
auth_token = os.environ.get("AUTH_TOKEN") #UR AUTH TOKEN


weather_params = {
    "lat": 25.761681,
    "lon": -80.191788,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = (response.json())

# print(weather_data ["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="bring an umbrella☔️",
        from_='+15512499580',
        to='+918851581535'
    )
