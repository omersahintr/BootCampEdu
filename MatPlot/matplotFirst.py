import matplotlib as mp
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import requests as rq
from io import StringIO

start_date = "2025-02-06%2010:00:00"
end_date = "2025-02-07%2010:00:00"
max_mag = 9.0
min_mag = 2.0
url = f"https://servisnet.afad.gov.tr/apigateway/deprem/apiv2/event/filter?minmag={min_mag}&maxmag={max_mag}&start={start_date}&end={end_date}&format=csv"

s = rq.get(url).text
c = pd.read_csv(StringIO(s))
print(c[["Date","Rms","Location","Magnitude"]])





