import numpy as np
import pandas as pd



dict = {"Neo":[30,50,np.nan], "Morpheus":[10,np.nan,40], "Trinity":[20,30,40]}

data_frame = pd.DataFrame(dict)

print(data_frame)
                #     Neo  Morpheus  Trinity
                # 0  30.0      10.0       20
                # 1  50.0       NaN       30
                # 2   NaN      40.0       40

# dropna() method:
print(data_frame.dropna())
                #     Neo  Morpheus  Trinity
                # 0  30.0      10.0       20

print(data_frame.dropna(axis=1))
                #    Trinity
                # 0       20
                # 1       30
                # 2       40
 # with more NaN counts data
new_dict = {"Neo":[30,50,np.nan], "Morpheus":[10,np.nan,40], "Trinity":[20,30,40], "Smith":[15,np.nan,np.nan]}
new_data_frame = pd.DataFrame(new_dict)

print(new_data_frame.dropna(axis=1, thresh=2)) # 2 and more NaN's has dropped. Smith's data removed.
                #     Neo  Morpheus  Trinity
                # 0  30.0      10.0       20
                # 1  50.0       NaN       30
                # 2   NaN      40.0       40

print(new_data_frame.dropna(axis=1, thresh=1))
                #     Neo  Morpheus  Trinity  Smith
                # 0  30.0      10.0       20   15.0
                # 1  50.0       NaN       30    NaN
                # 2   NaN      40.0       40    NaN

# fillna() methods:
print(new_data_frame.fillna(20))
                #     Neo  Morpheus  Trinity  Smith
                # 0  30.0      10.0       20   15.0
                # 1  50.0      20.0       30   20.0
                # 2  20.0      40.0       40   20.0

# Group Data Operations
sales_data = {"Code":["C++","PHP","Python","PHP","C++","PHP"],"Names":["Neo","Morpheus","Trinity","Smith","Adam","Joe"], "Money":[250,120,200,350,300,100]}
sales_data_frame = pd.DataFrame(sales_data)
print(sales_data_frame)
                #      Code     Names  Money
                # 0     C++       Neo    250
                # 1     PHP  Morpheus    120
                # 2  Python   Trinity    200
                # 3     PHP     Smith    350
                # 4     C++      Adam    300
                # 5     PHP       Joe    100

groups = sales_data_frame.groupby("Code")

print(groups.count())
                #         Names  Money
                # Code
                # C++         2      2
                # PHP         3      3
                # Python      1      1

print(groups.mean("Money"))
                #         Money
                # Code
                # C++     275.0
                # PHP     190.0
                # Python  200.0

print(groups.min("Money"))
                #         Money
                # Code
                # C++       250
                # PHP       100
                # Python    200

print(groups.max(numeric_only=True))
                #         Money
                # Code
                # C++       300
                # PHP       350
                # Python    200

print(groups.describe())
#        Money
#        count   mean         std    min    25%    50%    75%    max
# Code
# C++      2.0  275.0   35.355339  250.0  262.5  275.0  287.5  300.0
# PHP      3.0  190.0  138.924440  100.0  110.0  120.0  235.0  350.0
# Python   1.0  200.0         NaN  200.0  200.0  200.0  200.0  200.0

print(groups.describe().transpose())
                # Code                C++        PHP  Python
                # Money count    2.000000    3.00000     1.0
                #       mean   275.000000  190.00000   200.0
                #       std     35.355339  138.92444     NaN
                #       min    250.000000  100.00000   200.0
                #       25%    262.500000  110.00000   200.0
                #       50%    275.000000  120.00000   200.0
                #       75%    287.500000  235.00000   200.0
                #       max    300.000000  350.00000   200.0

