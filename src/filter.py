import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd
def user_filter(dataset):
    User_filter = {"float shares":(input("enter the float value you want the stocks to have less then or equal to")),
    "Country":"United States",
    "Sector":"Technology",
    "Industry":"",}
    user_dataset = {"Symbol":[], "Name":[],
    "Country":[],
    "Sector":[],
    "Industry":[],
    "float shares":[]
    }
    if User_filter["float shares"] =="":
        User_filter["float shares"] = dataset["float shares"].max()
    else:
        User_filter["float shares"] = float(User_filter["float shares"])*(10**6)
    for index,val in enumerate(dataset["float shares"]):
        if val<=User_filter["float shares"] and val !=float("nan"):
            for key in user_dataset.keys():
                user_dataset[key].append(dataset[key][index])
    for col in ["Country","Sector","Industry"]:
        if User_filter[col]!="":
            temp = {"Symbol":[], "Name":[],
            "Country":[],
            "Sector":[],
            "Industry":[],
            "float shares":[]
            }
            for index,val in enumerate(user_dataset[col]):
                if val == User_filter[col]:
                    for key in user_dataset.keys():
                        temp[key].append(user_dataset[key][index])
            user_dataset = temp
    user_dataset = pd.DataFrame(user_dataset)
    period = "15mn"
    want = 0
    user_dataset
    import yfinance as yf
    vol = []
    for tick in user_dataset["Symbol"]:
        try:
            vol.append(yf.Ticker(tick).history(period="15mn")["Volume"][0])
        except:
            vol.append(float("nan"))
    user_dataset["Volume"] = vol
    user_dataset.dropna(inplace=True)
    user_dataset.sort_values(by=["Volume"],ascending=False,inplace=True)
    article = []
    published_today = []
    for sym in user_dataset.Symbol:
        try:
            published_today.append(datetime.fromtimestamp(yf.Ticker(sym).news[0]["providerPublishTime"]).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]==datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0])
        except:
            published_today.append(False)
        try:
            # published_today.append(datetime.fromtimestamp(yf.Ticker(sym).news[0]["providerPublishTime"]).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]==datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0])
            url = yf.Ticker(sym).news[0]["link"]
            # print(url)
            # print(sym)
            data = requests.get(url)
            data = bs(data.content)
        
            article.append(data.find("div",{'class':'caas-body'}).text)
        except:
            # published_today.append("")
            article.append(float("nan"))
    # data 
    # data.div
    user_dataset["Published today"] = published_today
    user_dataset["Article"] = article
    return user_dataset
