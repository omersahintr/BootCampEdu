import pandas as pd
import numpy as np

## Pandas DataFrames:

data1 =  np.array([[1,2,3],[0,3,2],[8,9,7],[3,5,8]])

data_frame1 = pd.DataFrame(data1)

print(data_frame1[1][2]) # : 9

print(data_frame1) #       0  1  2
                      # 0  1  2  3
                      # 1  0  3  2
                      # 2  8  9  7
                      # 3  3  5  8

## Pandas DataFrame row-name and column-name define:

data =  np.array([[1,2,3,2],[1,0,3,2],[3,8,9,7],[3,5,8,9]])
name_data = ["Neo","Morpheus","Smith","Trinity"]
period_data = ["January","February","March","April"]

data_frame = pd.DataFrame(data, index=name_data, columns=period_data) #column and row name has defined


print(data_frame)
                    #               January  February  March  April
                    #Neo                1         2      3      2
                    #Morpheus           1         0      3      2
                    #Mr.Anderson        3         8      9      7
                    #Trinity            3         5      8      9

print(f"Neo on March {(data_frame["March"]).Neo}") # : Neo on March 3

print(data_frame["March"]["Neo"]) # : 3 --same to up


print(data_frame["April"])
                                # Neo            2
                                # Morpheus       2
                                # Mr.Anderson    7
                                # Trinity        9

print((data_frame["April"].mean())) # 5.0

print((data_frame.loc["Neo"])) #: Neo's values by months
                                # January     1
                                # February    2
                                # March       3
                                # April       2

print((data_frame.loc["Neo"]).mean()) # : 2.0
print((data_frame.iloc[0]).mean()) # : 2.0


# new column adding:
data_frame["May"] = data_frame["April"] * 2 # : create new month and April x 2
print(data_frame)
                #              January  February  March  April  May
                # Neo                1         2      3      2    4
                # Morpheus           1         0      3      2    4
                # Mr.Anderson        3         8      9      7   14
                # Trinity            3         5      8      9   18


# drop row operations:
print(data_frame.drop(labels="Neo", axis=0))
                #              January  February  March  April  May
                # Morpheus           1         0      3      2    4
                # Smith              3         8      9      7   14
                # Trinity            3         5      8      9   18

# drop column operations:
print(data_frame.drop(labels="February",axis=1))
                #              January  March  April  May
                # Neo                1      3      2    4
                # Morpheus           1      3      2    4
                # Smith              3      9      7   14
                # Trinity            3      8      9   18


# drop column operations changes original data
data_frame.drop(labels="April",axis=1, inplace=True)
print(data_frame)
                # January  February  March  May
                # Neo             1         2      3    4
                # Morpheus        1         0      3    4
                # Smith           3         8      9   14
                # Trinity         3         5      8   18