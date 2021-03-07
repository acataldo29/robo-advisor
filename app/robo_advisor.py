# this is the "app/robo_advisor.py" file

from dotenv import load_dotenv
import requests
import pandas
import json
import os
import csv


load_dotenv()

# User Defined Function to capture necessasry info from JSON file
#def price_info(symbol, )

symbol = input("Please input the stock symbol you wish to search: ") #.split(";", 3)

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="IBM")

if len(list(symbol)) > 1 and len(list(symbol)) < 5:
        stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&datatype=json&apikey={ALPHAVANTAGE_API_KEY}"
        response = requests.get(stocks_url)
        stock_info = json.loads(response.text)
else:
        quit()

print(stock_info.keys())
prices = []
for date, daily_data in stock_info["Time Series (Daily)"].items():
        record = {
                "date": date,
                "open": float(daily_data["1. open"]),
                "high": float(daily_data["2. high"]),
                "low": float(daily_data["3. low"]),
                "close": float(daily_data["4. close"]),
                "volume": int(daily_data["5. volume"]),
        }
        prices.append(record)


prices_df = pandas.DataFrame(prices)
prices_df.to_csv(f"data/prices_{symbol}.csv")






#for i in price

#csv_file_path = f"~/Desktop/Georgetown/Senior_Year/Spring_2021/OPIM_243/robo-advisor/data/prices_{symbol}.csv"
#with open(f"data/prices_{symbol}.csv", "w") as csv_file:
       #writer = csv.DictWriter(csv_file, fieldnames=stock_info.keys())
       #writer.writeheader()
       #writer.writerows(stock_info)


#if len(symbol) > 1:
#        for i in range(0, len(symbol)):
#                stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol[i]}&apikey={ALPHAVANTAGE_API_KEY}"
#                response = requests.get(stocks_url)
#                stock_info = json.loads(response.text)
#                print(type(stock_info))
#                print(stock_info)
#else:
#        stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
#        response = requests.get(stocks_url)
#        stock_info = json.loads(response.text)
#        print(type(stock_info))
#        print(stock_info)


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