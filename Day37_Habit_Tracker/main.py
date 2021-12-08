import requests
import datetime
USERNAME = "sioux"
TOKEN = "thisisa100dayofcodetoken"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": "sioux",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}
headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(graph_endpoint,json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?")
}
pixel_response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)

#pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
# update_data = {
#     "quantity": "5"
# }
# pixel_update_response = requests.put(pixel_update_endpoint, json=update_data, headers=headers)
# print(pixel_update_response.text)

# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)

