# this is the "app/robo_advisor.py" file

from dotenv import load_dotenv
import requests
import pandas
import json
import os

load_dotenv()

symbol = input("Please input the stock symbol(s) you wish to search (separated by ;): ").split(";", 3)

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="IBM")

#for i in range(0,len(symbol)):
#    print(f"Stock Symbol: {symbol[i]}")



if len(symbol) > 1:
    for i in range(0, len(symbol)):
        stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol[i]}&apikey={ALPHAVANTAGE_API_KEY}"
        response = requests.get(stocks_url)
        stock_info = json.loads(response.text)
        print(type(stock_info))
        print(stock_info)
else:
        stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
        response = requests.get(stocks_url)
        stock_info = json.loads(response.text)
        print(type(stock_info))
        print(stock_info)


#for i in symbol:
#    if i in stocks:
#        print() 






print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")