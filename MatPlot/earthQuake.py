import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests as rq
from io import StringIO
import datetime as dt


def earth_quake():
    now = dt.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    start_date = "2025-02-01%2000:00:00"
    end_date = f"{year}-{month}-{day}%20{hour}:{minute}:{second}"
    locat = "Ege Denizi"
    # end_date = "2025-02-02%2000:00:00"
    max_mag = 9.0
    min_mag = 2.0
    url = f"https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?minmag={min_mag}&maxmag={max_mag}&start={start_date}&end={end_date}&format=csv"

    s = rq.get(url).text
    c = pd.read_csv(StringIO(s))
    pd.set_option('display.max_rows', None)

    date_time = c[["Date"]]
    location = c[["Location"]]
    eventID = c[["EventID"]]
    magnitude = c[["Magnitude"]]
    quake = (c[["Date", "Magnitude", "Location"]])
    quake_plt = quake.loc[quake["Location"] == locat]
    print(quake_plt)

    """plt.scatter(quake_plt["Date"], quake_plt["Magnitude"], color="red", label="Earthquake")
    plt.show()"""

    area = np.pi * (5 * quake_plt["Magnitude"]) ** 2
    colors = np.random.rand()
    plt.scatter(quake_plt["Date"], quake_plt["Magnitude"], alpha=0.5, c="red", label="Earthquake")
    plt.title("Ege Denizi Earthquake")
    plt.xlabel("Date")
    plt.ylabel("Magnitude")
    plt.show()


    # print(c[["Date","Rms","Location","Magnitude"]])


earth_quake()



