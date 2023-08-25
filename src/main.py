import pandas as pd
from os.path import join
import sys
import yfinance as yf
sys.path.insert(0,"/Users/williammckeon/Desktop/news-screener/src")
from updating_data import identitfing_tickers
if __names =="__main__":
    tickers = pd.read_csv("ticker_info.csv")
    

