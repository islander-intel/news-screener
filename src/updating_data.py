# data = identitfing_tickers("data/names.csv")
# data.data
from urllib.error import HTTPError
import yfinance as yf
import pandas as pd

class identitfing_tickers:
    def __init__(self,ticker_path,nrows = None):
        if nrows==None:
            self.data = pd.read_csv(ticker_path,)
        else:
            self.data = pd.read_csv(ticker_path,nrows=nrows)
        self.building_dataset()
    def building_dataset(self):
        names = list(self.data.Symbol)
        float_vales = []
        # count = 0
        count = 1
        for i in names:
            print(f"currently on {i} {count}/{len(names)}, {(count/len(names))*100}%")

            finished = False
            while finished is False:
                try:
                    ticker = str(i.strip())
                    data = yf.Ticker(ticker)
                    if "floatShares" in data.info.keys():
                        val = data.info["floatShares"]
                        # print(val)
                    else:
                        val = None
                    float_vales.append(val)
                    finished= True
                    count+=1
                except:
                    pass
            
            # if count == 10:
            #     break
            # else:
            #     count+=1
        self.data["float shares"] = float_vales
# data = identitfing_tickers("data/names.csv")
# data.data