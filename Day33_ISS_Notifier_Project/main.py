import requests
from datetime import datetime
import time
import smtplib

MY_EMAIL = "lientrankim95@gmail.com"
MY_PASSWORD = ""
gmail_smtp = "smtp.gmail.com"
MY_LAT = 16.054407 # Your latitude
MY_LONG = 108.202164 # Your longitude

def is_iss_overheat():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True

def is_night():
    parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
#Your position is within +5 or -5 degrees of the ISS position.
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overheat() and is_night():
        with smtplib.SMTP(gmail_smtp) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="siouxtest05@gmail.com", msg=f"Subject: ISS coming\n\nTHe ISS is above you in the sky")
    else:
        with smtplib.SMTP(gmail_smtp) as connection:
            connection.starttls()  
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="siouxtest05@gmail.com", msg=f"Subject: ISS is far away\n\nIss is far from your place")
    