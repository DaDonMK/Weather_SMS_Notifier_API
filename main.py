import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api = "85ae73c8dbb8e5fe8cf51bf0e607f330"
ACCT_SID = "AC128f822a0d2bca2f53443d2f3e6e64e7"
TOKEN = "c3ce19d1f1d804b96253ffc5e9ddd418"

weather_params = {
    "lat": 32.776665,
    "lon": -96.796989,
    "exclude": "current,minutely,daily",
    "appid": api
}

response = requests.get(OWM_Endpoint, params=weather_params)
data = response.json()

id = []

for x in range(12):
    id.append(data["hourly"][x]["weather"][0]["id"])

print(id)
umbrella = False
for x in id:
    if (x < 700):
        umbrella = True

if (umbrella == True):
    client = Client(ACCT_SID, TOKEN)
    message = client.messages \
        .create(
        body="It's going to RAIN or SNOW today in Dallas. Remember to bring an umbrella! ☔️",
        from_='+17144850920',
        to='+19726163647'
    )
    print(message.status)
