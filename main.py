import requests
from twilio.rest import *

VIRTUAL_TWILIO_NUMBER = "+12565884698"
VERIFIED_NUMBER = "9746558679"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "BEV1FE89C8NG0E2Y"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "AC4c7fc74c5bc8a448e74dabc2fed7aea3"
TWILIO_AUTH_TOKEN = "31200bc81fa562c7d8cca8a1fa7b4547"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# positive difference  between closing price
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

