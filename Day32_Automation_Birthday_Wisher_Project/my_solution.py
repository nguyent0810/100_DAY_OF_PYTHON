import random
import pandas
import smtplib
import datetime as dt
##################### Extra Hard Starting Project ######################
MY_EMAIL = ""
MY_PASSWORD = ""
gmail_smtp = "smtp.gmail.com"
lettes = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")
birthday_list = df.values.tolist()
print(birthday_list[0])
# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now().strftime('%m-%d')
for item in birthday_list:
    birth_day = dt.datetime(year=item[2], month=item[3], day=item[4]).strftime('%m-%d')
    if today == birth_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        recipent = item[1]
        random_letter = random.choice(lettes)
        with open (f"letter_templates/{random_letter}") as data:
            template = data.read()
            content = template.replace("[NAME]", item[0])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(gmail_smtp) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=recipent, msg=f"Subject: Happy birthday {item[0]}\n\n{content}")




