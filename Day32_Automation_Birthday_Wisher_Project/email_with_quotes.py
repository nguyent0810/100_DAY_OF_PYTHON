import smtplib
import datetime as dt
import pandas
import random
import calendar
MY_EMAIL = "lientrankim95@gmail.com"
MY_PASSWORD = "PoGI2g6cca93mrokMRAB"
gmail_smtp = "smtp.gmail.com"
recipent = "siouxtest05@gmail.com"
#mail_content = "Subject:Random quote\n\n"

week_day = dt.datetime.now().weekday()
# Option 1: to get day in English
current_day = calendar.day_name[week_day]
# Option 2: to get day in English https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# current_day = dt.datetime.today().strftime('%A')
# To list in PANDA
# df = pandas.read_csv("quotes.txt")
# df_list = df.values.tolist()
# quote_list = [item[0] for item in df_list]
with open("quotes.txt") as data:
    all_quotes = data.readlines()
    quote = random.choice(all_quotes)
mail_content = f"Subject:{current_day}\n\n{quote}"
if week_day == 1:

    with smtplib.SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=recipent, msg=mail_content)

# print(dt.datetime.now())

# date_of_birth = dt.datetime(year=1996, month=5, day=18)
# print(date_of_birth)