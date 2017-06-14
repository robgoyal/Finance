# Name: history.py
# Author: Robin Goyal
# Last-Modified: June 13, 2017
# Purpose: Get stock history data

import datetime
import sys
from csv import reader
from pandas_datareader import data
from matplotlib import pyplot

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
        dates = [i[0] for i in data]
        prices = [i[4] for i in data]


def main(symbol):
    history(symbol, 3)
    plotHistory(symbol)

if __name__ == "__main__":
    main(str(sys.argv[1]))