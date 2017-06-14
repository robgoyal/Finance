# Name: history.py
# Author: Robin Goyal
# Last-Modified: June 13, 2017
# Purpose: Retrieve and plot stock history data

import datetime
import sys
from csv import reader
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from dateutil import parser

def history(symbol, years):

    # Create csv_path
    csv_path = "history/{}.csv".format(symbol)

    # Create datetimes
    today = datetime.date.today()
    start = datetime.datetime(today.year - years, today.month, today.day)
    end = datetime.datetime(today.year, today.month, today.day)

    try:
        # Retrieve quote history and write to csv file following csv path
        stock_history = data.DataReader(symbol, 'google', start, end)
        stock_history.to_csv(csv_path)

    except:
        # Stock doesn't exist
        print("Error: Stock Doesn't Exist")

def plotHistory(symbol):

    # Open csv file 
    with open("history/{}.csv".format(symbol), 'r') as f:
        data = list(reader(f))

        # Get dates and prices of data
        dates = [parser.parse(i[0]) for i in data[1::]]
        prices = [i[4] for i in data[1::]]


    # Prepare plot
    fig, ax = plt.subplots()
    ax.plot(dates, prices)

    # Set date axis formatting
    fig.autofmt_xdate()
    ax.xaxis.set_major_formatter(DateFormatter("%b-%Y"))

    # Set title and labels
    plt.title("{} Price History".format(symbol))
    plt.ylabel("Price (USD)")
    
    # Show plot
    plt.show()

def main(symbol):
    history(symbol, 3)
    plotHistory(symbol)

if __name__ == "__main__":
    main(str(sys.argv[1]))