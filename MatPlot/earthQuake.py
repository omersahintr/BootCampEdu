import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests as rq
from io import StringIO
import datetime as dt
from mpl_toolkits.mplot3d import axes3d



def earth_quake():
    now = dt.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    start_date = "2025-04-22%2000:00:00"
    end_date = f"{year}-{month}-{day}%20{hour}:{minute}:{second}"
    locat = "Marmara Denizi"
    # end_date = "2025-01-15%2000:00:00"
    max_mag = 9.0
    min_mag = 3.0
    url = f"https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?minmag={min_mag}&maxmag={max_mag}&start={start_date}&end={end_date}&format=csv"

    s = rq.get(url).text
    c = pd.read_csv(StringIO(s))
    pd.set_option('display.max_rows', None)

    date_time = c[["Date"]]
    location = c[["Location"]]
    eventID = c[["EventID"]]
    magnitude = c[["Magnitude"]]
    quake = (c[["Date", "Magnitude", "Location","Depth"]])
    quake_plt = quake.loc[quake["Location"] == locat]
    print(quake_plt)

    """plt.scatter(quake_plt["Date"], quake_plt["Magnitude"], color="red", label="Earthquake")
    plt.show()"""
    
    #plt.scatter(quake_plt["Date"], quake_plt["Magnitude"], alpha=0.5, c="red", label="Earthquake")
    #plt.plot(quake_plt["Date"], quake_plt["Magnitude"], marker="x", linestyle=":", color="#00AA11", label="Earthquake")

    """
    plt.title(f"{locat} Earthquake")
    plt.xlabel("Date")
    plt.ylabel("Magnitude")

    x = quake_plt["Depth"]
    y = quake_plt["Magnitude"]

    fig,ax = plt.subplots()

    ax.triplot(x,y)
    ax.set(xlim=(-5,20),ylim=(-5,15))"""

    plt.style.use('_mpl-gallery')

    X = quake_plt["Depth"]
    Y = quake_plt["Magnitude"]
    Z = quake_plt["Depth"]

    fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
    ax.plot_wireframe(X,Y,Z,rstride=10,cstride=10)

    ax.set(xticklabels=[],
           yticklabels=[],
           zticklabes=[])


    plt.show()


    # print(c[["Date","Rms","Location","Magnitude"]])


earth_quake()



