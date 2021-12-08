import requests
import datetime

GENDER = ""
WEIGHT_KG = int
HEIGHT_CM = int
AGE = 34
APP_ID = ""
API_KEY = ""
username = ""
project_name = ""
sheet_name = ""
sheety_endpoint = f"https://api.sheety.co/{username}/{project_name}/{sheet_name}"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_test = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_test,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

print(result)
headers = {
    "Authorization": "Basic c2lvdXh0ZXN0MDU6c2lvdXgxMTEx"
    }

today = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheety_parameters = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise":  exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }


sheety_response = requests.post(sheety_endpoint, json=sheety_parameters, headers=headers)
print(sheety_response)