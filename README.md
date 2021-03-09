# Robo Advisor Application

This application will provide clients with recommendations to their portfolio. Mainly, this app will allow users to input a stock's symbols and provide some statistics for that stock along with a recommendation of whether or not to buy. Further, we'll save a .csv file of price data from the past 100 days, and create a graph showing the closing prices.

# Setup

To start, we will need to set up this virtual repository as a local one to your computer. First, navigate to your desired location within the terminal:

```sh
cd ~/Desktop/your/desired/path
```

Next, you need to clone the repository to your own local computer. You can enter the following commands in the terminal to do so:

```sh
git clone https://github.com/acataldo29/robo-advisor
```

This will clone the repository and save it to the location you specified previously. Next, you'll want to navigate to that repository. Enter the following into your terminal:

```sh
cd ~/Desktop/your/desired/path/robo-advisor
```
In this repository, there are a few directories and a few files. The data directory is where the program will store a .csv file containing various prices for your selected stock from the last 100 days. The plots directory will contain line plots of the closing prices for your desired stock. Finally, the app directory contains the python code to execute the application.

Next, we will need to set up your environment. We need to do this in order to create environment variables. Enter the following into your terminal:

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```

Now, we can install the third-party packages located within the 'requirements.txt' file. Enter the following into your terminal:

```sh
pip install -r requirements.txt
```

## API

Next, you'll need to set up your API. For this program, we'll be using an Alpha Vantage API. You can get one for free by going to https://www.alphavantage.co/support/#api-key and entering some information. 

This key will allow us to access and download the stock data that is necessary to give the recommendation. 

Now, we will create a '.env' file and store your API key as an environment variable. Your current working directory should be the root depository (robo-advisor). In your terminal, type:

```sh
touch .env
```

Now, in your code editor, open the repository and .env file. In the file, enter:

```sh
ALPHAVANTAGE_API_KEY="your API key"
```

## Using the Application

To access this application, type the following in your command prompt:

```sh
python app/robo_advisor.py
```

You will be asked to enter the stock symbol you wish to search. The program allows for a symbol of up to 5 letters, however you can adjust this boundary by editing line 33 of 'app/robo-advisor.py' to your desired length.

After entering your desired symbol, you should see this output:

```
Please input the stock symbol you wish to search: IBM
-------------------------
SELECTED SYMBOL: IBM
-------------------------
REQUESTING STOCK MARKET DATA...
REQUEST AT: 2021-03-08 09:28 PM
-------------------------
LATEST DAY: 2021-03-08
LATEST CLOSE: $124.81
RECENT HIGH: $132.24
RECENT LOW: $130.05
-------------------------
CONFIDENCE LEVEL: Medium
REASON: IBM's latest closing price was greater than 75% of the recent high, but less than 95%
-------------------------
```

The program will also save the data to data/prices_{selected stock}, and plots to plot/prices_plot_{selected stock}. It will then ask you if you'd like to input another stock. 

You may enter as many stocks as you'd like to search, and the program will repeat for each one. When you wish to search no more stocks, simply type "N" when asked if you'd like to search for another symbol.

Enjoy, and good luck investing!