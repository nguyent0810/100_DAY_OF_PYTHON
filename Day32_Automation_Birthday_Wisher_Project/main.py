##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
MY_EMAIL = "lientrankim95@gmail.com"
MY_PASSWORD = "PoGI2g6cca93mrokMRAB"
gmail_smtp = "smtp.gmail.com"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP(gmail_smtp) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person.email, msg=f"Subject: Happy birthday\n\n{contents}")


