# Name: history.py
# Author: Robin Goyal
# Last-Modified: June 15, 2017
# Purpose: Retrieve and plot stock history data

import datetime
import requests_cache
import matplotlib.pyplot as plt
import base64
import io

from csv import reader
from pandas_datareader import data
from matplotlib.dates import DateFormatter
from dateutil import parser

def get_history(stock):

    # Get name and symbol from parameter
    name = stock['name']
    symbol = stock['symbol']

    # Create csv_path
    csv_path = "history/{}.csv".format(symbol)

    # Create datetimes
    today = datetime.date.today()
    start = datetime.datetime(today.year - 3, today.month, today.day)
    end = datetime.datetime(today.year, today.month, today.day)

    # Cache responses
    expire_after = datetime.timedelta(days=3)
    session = requests_cache.CachedSession(cache_name='cache', \
                backend='sqlite', expire_after=expire_after)

    try:
        # Retrieve quote history and write to csv file following csv path
        stock_history = data.DataReader(symbol, 'google', start, end, session=session)
        stock_history.to_csv(csv_path)

        return plot_history(name, symbol)

    except:
        # Stock doesn't exist
        print("Error: Stock Doesn't Exist")

def plot_history(name, symbol):

    # Open csv file 
    with open("history/{}.csv".format(symbol), 'r') as f:
        data = list(reader(f))

        # Get dates and prices of data
        dates = [parser.parse(i[0]) for i in data[1::]]
        prices = [i[4] for i in data[1::]]


    # Prepare plot
    fig, ax = plt.subplots()
    ax.plot(dates, prices, lw=1.0, color = (214/255, 39/255, 40/255))

    # Set date axis formatting
    fig.autofmt_xdate()
    ax.xaxis.set_major_formatter(DateFormatter("%b-%Y"))

    # Set title and labels
    plt.title("{} Price History".format(name), fontsize=18)
    plt.ylabel("Price (USD)")
    
    # Remove plot frame lines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Create png image of plot
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches="tight")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return plot_url