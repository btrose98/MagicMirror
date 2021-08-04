#Need to install the following:
#pip install pandas
#pip install pandas-datareader

import pandas as pd
import pandas_datareader.data as dr
import datetime as dt

class yahooApiCall:

    startTime = dt.datetime(2021, 7, 29)
    endTime = dt.datetime.today()
    ticker = input("Please enter ticker: ")

    df = dr.DataReader(ticker, 'yahoo', startTime, endTime)
    
    print(df)