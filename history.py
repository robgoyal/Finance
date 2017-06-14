# Name: history.py
# Author: Robin Goyal
# Last-Modified: June 13, 2017
# Purpose: Get stock history data

from pandas_datareader import data
import datetime

def history(symbol, years):

    csv_path = "history/{}.csv".format(symbol)

    today = datetime.date.today()
    start = datetime.datetime(today.year - years, today.month, today.day)
    end = datetime.datetime(today.year, today.month, today.day)

    try:
        stock_history = data.DataReader(symbol, 'google', start, end)
        stock_history.to_csv(csv_path)
    except:
        print("Error: Stock Doesn't Exist")

history("TESLA", 3)

