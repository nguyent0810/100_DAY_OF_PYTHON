import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "0W8MC7EI4Q63OU8B"
NEWS_API_KEY = "33a53d27f2c443fb8acf4bbd1c585057"

account_sid = "ACc8d0565c05dd3bef552b994d89f5cbeb"
auth_token = "259b8844158beaed20557955126a8eff"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
news_param = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else: 
    up_down = "🔻"

diff_percent = (difference / float(yesterday_closing_price)) * 100
if abs(diff_percent) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK}: {up_down}{round(diff_percent)}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body=article,
                            from_='+13253355251',
                            to='+84949837611'
                        )