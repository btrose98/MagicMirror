#Need to install the following:
#pip install pandas
#pip install pandas-datareader


import pandas as pd
import pandas_datareader.data as dr
import datetime as dt
import math

class yahooApiCall:

    stockList = ['AAPL', 'TSLA', 'BB']
    openList = []
    closeList = []

    end = dt.date.today()
    start = end - dt.timedelta(days=1)

    df = dr.DataReader(stockList, 'yahoo', start, end)
   

    tickers = df.columns.levels[1]
    date = end

    #works
    for i in range(len(stockList)):
        openPrice = df['Open'][stockList[i]]
        
        openList.append(round(*openPrice,2))
    
    for j in range(len(stockList)):
        closePrice = df['Close'][stockList[j]]
        closeList.append(round(*closePrice,2))