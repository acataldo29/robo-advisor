# this is the "app/robo_advisor.py" file

from dotenv import load_dotenv
import requests
import pandas
import json
import os
import csv
from datetime import datetime


load_dotenv()

############## User Defined Functions ##############
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 
############## User Input/Data Handling ############
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="IBM")

while True:
        symbol = input("Please input the stock symbol you wish to search: ") # .split(";", 3)
        if len(list(symbol)) > 1 and len(list(symbol)) < 5:
                stocks_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&datatype=json&apikey={ALPHAVANTAGE_API_KEY}"
                response = requests.get(stocks_url)
                stock_dict = json.loads(response.text)
                print(stock_dict.keys())
        else:
                print("That input is invalid. Please try again")
                input("Please input the stock symbol you wish to search: ") # .split(";", 3)

        prices = []
        for date, daily_data in stock_dict["Time Series (Daily)"].items():
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

        ############## Print Necessary Information ##############
        print("-------------------------")
        print(f"SELECTED SYMBOL: {symbol}")
        print("-------------------------")
        print("REQUESTING STOCK MARKET DATA...")
        today = datetime.now()
        today = today.strftime("%Y-%m-%d %I:%M %p")
        print(f"REQUEST AT: {today}")
        print("-------------------------")
        print("LATEST DAY:", prices_df["date"].max())
        print("LATEST CLOSE:", to_usd(prices_df["close"][0]))
        print("RECENT HIGH:", to_usd(prices_df["high"].max()))
        print("RECENT LOW:", to_usd(prices_df["low"].max()))
        print("-------------------------")
        #create recommendation criteria
        if prices_df["close"][0]/prices_df["high"].max() > 0.95:
                print("CONFIDENCE LEVEL: High")
                print(f"REASON: {symbol}'s latest closing price was greater than 25% of the recent high")
                print("-------------------------")        
        elif prices_df["close"][0]/prices_df["high"].max() > 0.75:
                print("CONFIDENCE LEVEL: Medium")
                print(f"REASON: {symbol}'s latest closing price was greater than 75% of the recent high, but less than 95%")
                print("-------------------------")
        else:
                print("CONFIDENCE LEVEL: Low")
                print(f"REASON: {symbol}'s latest closing price was less than 75% of the recent high")
                print("-------------------------")


        additional = input("Would you like to search for another symbol? [Y/N]: ")
        if additional == "N":
                break
                exit()    
        elif additional not in ("Y", "N"):
                print("That inupt is invalid. Please try again")
                input("Would you like to search for another symbol? [Y/N]: ")
        else:
                True
                symbol
        
                
