import pandas as pd
from os.path import join
import sys
import yfinance as yf
sys.path.insert(0,"/Users/williammckeon/Desktop/news-screener/src")
from updating_data import identitfing_tickers
origin = pd.read_csv("stock_origin.csv")
final_columns = ['Symbol', 'Name','Country','Sector', 'Industry']
drop_list = [i for i in origin.columns if i not in final_columns]
origin.drop_duplicates(inplace=True)
origin.drop(columns=drop_list,inplace=True)
drop_index = [index for index in origin.Symbol.index if isinstance(origin.Symbol[index],str) and "^" in origin.Symbol[index] or isinstance(origin.Symbol[index],str) and "/" in origin.Symbol[index] or isinstance(origin.Symbol[index],float)]
origin.drop(drop_index, inplace = True)
origin.dropna(inplace = True)
# names = origin.iloc[:,0].values
# float_vales = []
# count = 0
# for i in names:
#     data = yf.Ticker(i)
#     if "floatShares" in data.info.keys():
#         # print("yes")
#         val = data.info["floatShares"]
#         print(val)
#     else:
#         val = None
#     float_vales.append(val)
#     if count == 10:
#         break
#     else:
#         count+=1
origin.to_csv(join("data","final.csv"),index=False)
data = identitfing_tickers("data/final.csv")
data.data
# for i in data["floate shares"].index:
#     if data["floate shares"][i]:
#         print(data.Symbol[i])
data.data.to_csv("ticker_info.csv",index=False)