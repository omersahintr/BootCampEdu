# IMPORT MODULES: @requests, @matplotlib, @pandas, @datetime
import requests as req
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import datetime as dt

# VARIABLES:
start_date_year = "2024"
start_date_month = "10"
start_date_day = "01"
start_date_hour = "20"
start_date_minute = "00"
start_date_second = "00"

now = dt.datetime.now()
end_date_year = str(now.year)
end_date_month = str(now.month)
end_date_day = str(now.day)
end_date_hour = str(now.hour)
end_date_minute = str(now.minute)
end_date_second = str(now.second)

locator = "Ege Denizi"
mag = 3.0

# RESPONSE FUNCTION:
def response_url():
    i=0
    data_frame = pd.DataFrame()
    dict = {}
    url = f"https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?start={start_date_year}-{start_date_month}-{start_date_day}%20{start_date_hour}:{start_date_minute}:{start_date_second}&end={end_date_year}-{end_date_month}-{end_date_day}%20{end_date_hour}:{end_date_minute}:{end_date_second}" #for live data
    #print(req.get(url).status_code):
    
    plt.title(f"{locator} Depremler-{start_date_year}")
    plt.xlabel("Depth")
    plt.ylabel("Magnitude")
    response = req.get(url)
    if response.status_code == 200:   
        for query in response.json():
            if query["location"] != locator and float(query["magnitude"])>mag:
                i+=1
                plt.scatter((query["depth"]), float(query["magnitude"]), color="red")
                #plt.plot((query["date"])[0:10], float(query["magnitude"]), color="red")
                #print(f"{i} - {query["date"][0:10]}-{query["location"]}-{query["magnitude"]}--{query["depth"]}")
        plt.show()

response_url()