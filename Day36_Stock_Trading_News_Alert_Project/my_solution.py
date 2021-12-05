import requests
import datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_api_key =  "33a53d27f2c443fb8acf4bbd1c585057"
alpha_api_key = "0W8MC7EI4Q63OU8B"
account_sid = "ACc8d0565c05dd3bef552b994d89f5cbeb"
auth_token = "259b8844158beaed20557955126a8eff"
alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK, 
    "apikey": alpha_api_key
}
news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": news_api_key
}
alpha_url = 'https://www.alphavantage.co/query'
news_url = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



response = requests.get(alpha_url, params=alpha_parameters)
response.raise_for_status()
data = response.json()
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=3)
day_before_yesterday = yesterday - datetime.timedelta(days=1)
yesterday_close_price = float(data["Time Series (Daily)"][str(yesterday)]['4. close'])
day_before_yesterday_close_price = float(data["Time Series (Daily)"][str(day_before_yesterday)]['4. close'])
percentage_value = yesterday_close_price * 5 / 100
different_value = yesterday_close_price - day_before_yesterday_close_price
different_percentage = round(different_value / yesterday_close_price * 100)
if different_value < percentage_value * -1 or different_value > percentage_value:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_res = requests.get(news_url, params=news_parameters)
    news_res.raise_for_status()
    news_data = news_res.json()['articles'][:3]
    if different_percentage < 0:
        different_percentage = f"{STOCK}: 🔻 {different_percentage * -1}%"
    else:
        different_percentage = f"{STOCK}: 🔺 {different_percentage}%"
    for i in range(len(news_data)):
        headline = f"Headline: {news_data[i]['title']}"
        brief = f"Brief: {news_data[i]['description']}"
        content = f"{different_percentage}\n{headline}\n{brief}"
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=content,
                            from_='+13253355251',
                            to='+84949837611'
                        )



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

