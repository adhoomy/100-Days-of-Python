# number must be in twilio whatsapp server to receive messages

import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = ""  # enter company stock name in the quotes
COMPANY_NAME = ""  # enter company name in the quotes

today = datetime.now().date()
one_day = timedelta(days=1)
yesterday = today - one_day
before_yesterday = today - (one_day * 2)

stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ""  # enter api key for stock data api in the quotes
}
s_r = requests.get(stock_url, stock_params)

yesterdays_close = s_r.json()["Time Series (Daily)"][str(yesterday)]["4. close"]
before_yesterdays_close = s_r.json()["Time Series (Daily)"][str(before_yesterday)]["4. close"]

difference = float(yesterdays_close) - float(before_yesterdays_close)
percent_difference = (difference / float(before_yesterdays_close)) * 100
if abs(percent_difference) >= 5:
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,  # enter company name in the quotes
        "from": str(before_yesterday),
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": ""  # enter api key for news api in the quotes
    }
    n_r = requests.get(url=news_url, params=news_params)

    articles = n_r.json()["articles"][:3]
    formatted_articles = [f"Headline:\n{article['title']}\n\nBrief:\n{article['description']}" for article in articles]

    account_sid = ""  # enter api account sid in the quotes
    auth_token = ""  # enter api auth token in the quotes

    client = Client(account_sid, auth_token)
    if difference > 0:
        sign = "🔺"
    else:
        sign = "🔻"
    message = client.messages.create(
        from_="whatsapp:",  # enter number to send from in the quotes
        body=f"{STOCK}: {sign}{round(abs(percent_difference))}%",
        to="whatsapp:"  # enter number to send to in the quotes
    )
    for article in formatted_articles:
        message = client.messages.create(
            from_="whatsapp:",  # enter number to send from in the quotes
            body=article,
            to="whatsapp:"  # enter number to send to in the quotes
        )
