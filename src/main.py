import pandas as pd
from os.path import join
import sys
import yfinance as yf
sys.path.insert(0,"/Users/williammckeon/Desktop/news-screener/src")
from updating_data import identitfing_tickers
from filter import user_filter
if __name__ =="__main__":
    tickers = pd.read_csv("ticker_info.csv")
    final_dataset = user_filter(tickers)
    print(final_dataset.head(10))

