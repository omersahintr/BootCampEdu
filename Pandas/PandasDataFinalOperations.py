import pandas as pd
import numpy as np

new_dict1 = {"Name":["John","Alice","Bob","Doe","Smith"],
            "Sports":["Football","Basketball","Cricket","Tennis","Baseball"],
            "Calori":[230,240,220,250,260]
            }

new_dict2 = {"Name":["Jack","Adam","Brain","Doh","Sarah"],
            "Sports":["Football","Basketball","Cricket","Tennis","Baseball"],
            "Calori":[130,140,120,150,160]
            }

new_dict3 = {"Name":["Homer","Jason","Track","Dora","Fiona"],
            "Sports":["Football","Basketball","Cricket","Tennis","Baseball"],
            "Calori":[330,340,320,350,360]
            }

new_data_frame1 = pd.DataFrame(new_dict1)
new_data_frame2 = pd.DataFrame(new_dict2)
new_data_frame3 = pd.DataFrame(new_dict3)


#Concatenation of DataFrames
new_data_frame = pd.concat([new_data_frame1,new_data_frame2,new_data_frame3],ignore_index=True)

print(new_data_frame)
"""#####             Name      Sports  Calori
                0    John    Football     230
                1   Alice  Basketball     240
                2     Bob     Cricket     220
                3     Doe      Tennis     250
                4   Smith    Baseball     260
                5    Jack    Football     130
                6    Adam  Basketball     140
                7   Brain     Cricket     120
                8     Doh      Tennis     150
                9   Sarah    Baseball     160
                10  Homer    Football     330
                11  Jason  Basketball     340
                12  Track     Cricket     320
                13   Dora      Tennis     350
                14  Fiona    Baseball     360
#####"""

#Merging of DataFrames
merge_data_frame = pd.merge(new_data_frame1,new_data_frame2,on="Sports")

print(merge_data_frame)
"""####       Name_x      Sports  Calori_x Name_y  Calori_y
            0   John    Football       230   Jack       130
            1  Alice  Basketball       240   Adam       140
            2    Bob     Cricket       220  Brain       120
            3    Doe      Tennis       250    Doh       150
            4  Smith    Baseball       260  Sarah       160
#####"""

#unique values in the DataFrame
new_sales_dict = {"Name":["John","Alice","Bob","Doe","Smith"],"Sales":[230,240,220,250,260],"Profit":[30,40,20,50,60]}
new_sales_frame = pd.DataFrame(new_sales_dict)

print(new_sales_frame)
"""####     Name  Sales  Profit
            0  John    230      30
            1 Alice    240      40
            2   Bob    220      20
            3   Doe    250      50
            4 Smith    260      60
#####"""

print(new_sales_frame["Name"].unique()) 
# ['John' 'Alice' 'Bob' 'Doe' 'Smith']

print(new_sales_frame["Name"].nunique())
# 5

#VAT Calculation in DataFrame
def vat_calc(sales):
    return sales*0.18

print(new_sales_frame["Sales"].apply(vat_calc))
"""####     0    41.4
            1    43.2
            2    39.6
            3    45.0
            4    46.8
            Name: Sales, dtype: float64
#####"""
