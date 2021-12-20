import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "lientrankim95@gmail.com"
MY_PASSWORD = ""
gmail_smtp = "smtp.gmail.com"
url = "https://www.amazon.com/Lenovo-IdeaPad-Processor-Graphics-82KT00GVUS/dp/B09BG841VC/ref=sr_1_2?keywords=lenovo&qid=1639625186&sr=8-2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8,ja;q=0.7"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, features='lxml')
price = soup.find("span", class_="a-offscreen").getText()
actual_price = float(price.split("$")[1])
print(actual_price)
target_price = 700
if actual_price < target_price:
    with smtplib.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="siouxtest05@gmail.com", msg=f"The price now is {actual_price}. Get a go to buy it now!")

