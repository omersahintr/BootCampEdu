
import pandas as pd
import numpy as np

##Series ##
#Method-1
dictionary = {"http" : 80, "https" : 443, "rdc" : 3389, "smtp" : 25 }
print(pd.Series(dictionary)) #  http     80
                             #  https    443
                             #  rdc      3389
                             #  smtp     25
                             #  dtype: int64
#Method-2
ports = [80, 443, 3389, 25]
protocols = ["http", "https", "rdc", "smtp"]

print(pd.Series(index=protocols, data=ports)) #  http     80
                                              #  https    443
                                              #  rdc      3389
                                              #  smtp     25
                                              # dtype: object

##NumPy Array to Pandas Series

n_array = np.arange(20,70,10)
print(pd.Series(n_array)) # 0    20
                          # 1    30
                          # 2    40
                          # 3    50
                          # 4    60
                          # dtype: int64

##NumpyArray and Python List merge to Pandas Series:

nArray = np.array([10,20,30,40])
pList = ["Mercedes","BMW", "Tesla","Audi"]

pSeries = pd.Series(index=pList,data=nArray)
print(pSeries) # Mercedes    10
               # BMW         20
               # Tesla       30
               # Audi        40

print(pSeries["Tesla"]) # 30

## Series Math Operation:

race1 = pd.Series(data=[220,250,280], index=["Audi","Mercedes", "Tesla"])
race2 = pd.Series(data=[260,230,300], index=["Audi","Mercedes", "Tesla"])

result = race1 + race2

print(result)
print(f"Winner is {result[result == pd.Series.max(result)]}")

## Pandas Series Operations with Different indexes

series1 = pd.Series(data=[100,200,300], index=["London","Tokyo","New York"])
series2 = pd.Series(data=[140,250,410], index=["London","Tokyo","Istanbul"])

operation = series1 + series2

print(operation) # Istanbul      NaN
                 # London      240.0
                 # New York      NaN
                 # Tokyo       450.0
                 # dtype: float64