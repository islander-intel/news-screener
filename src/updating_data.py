# data = identitfing_tickers("data/names.csv")
# data.data
from urllib.error import HTTPError
import yfinance as yf
import pandas as pd

class identitfing_tickers:
    def __init__(self,ticker_path):
        self.data = pd.read_csv(ticker_path)
        self.building_dataset()
    def building_dataset(self):
        names = self.data.iloc[:,0].values
        float_vales = []
        for i in names:
            data = yf.Ticker(i)
            if "floatShare" in data.info.keys():
                val = data.info["floatShare"]
            else:
                val = None
            float_vales.append(val)
        self.data["float shares"] = float_vales

# data = identitfing_tickers("data/names.csv")
# data.data