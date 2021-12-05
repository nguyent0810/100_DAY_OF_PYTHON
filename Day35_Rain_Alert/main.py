import requests
import time
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ca7248ae17c657d8ac0a6ba1affc3438"
account_sid = "ACc8d0565c05dd3bef552b994d89f5cbeb"
auth_token = "259b8844158beaed20557955126a8eff"

#proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

parameters = {
    "lat": 16.054407,
    "lon": 108.202164,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}



response = requests.get(OWM_Endpoint ,params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
#weather_next_twelwe = [weather_data['hourly'][i] for i in range(0, 12)]
#print(weather_slice[0]['weather'][0]['id'])
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        rain_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(hour_data['dt']))
        #client = Client(account_sid, auth_token, http_client=proxy_client)
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=f"Bring the umbrela at {rain_time}",
                            from_='+13253355251',
                            to='+84949837611'
                        )

