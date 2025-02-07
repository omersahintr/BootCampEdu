import pandas as pd
import numpy as np
import openpyxl

data_frame = pd.read_excel("sales.xlsx")
print(data_frame)

# 1) How many rows of data are there in total?

count_rows = data_frame["Employee Name"].count()
print(f"Total Rows Count: {count_rows}")
                # Total Rows Count: 100

# 2) What is the average salary this company pays?

averaje_salary = data_frame["Salary"].mean()
print(f"Average Salary: {averaje_salary:.2f}")
                # Average Salary: 725.84

# 3) How does the average salary compare across departments at this company?

averaje_salary_of_department = data_frame.groupby("Department")["Salary"].mean()
print(f"Average Salary of Department: \n{averaje_salary_of_department.round(2)}")
"""             Average Salary of Department:
                Department
                Finance                 805.41
                HR                      640.94
                Marketing               707.00
                Sales                   656.67
                Software Development    826.41
                Name: Salary, dtype: float64
"""

# 4) How does the average salary compare by title (senior - junior) at this company?
averaje_salary_of_title = data_frame.groupby("Title")["Salary"].mean()
print(f"Average Salary of Title: \n{averaje_salary_of_title.round(2)}")
"""         Average Salary of Title: 
                Title
                C-level       1058.33
                Junior         440.62
                Mid            641.45
                Mid-Senior     725.50
                Senior         867.78
                Name: Salary, dtype: float64
"""

#5) On average, how many percent more salary does a senior person earn than a junior person?
match_avg = data_frame.groupby("Title")["Salary"].mean()
senior_avg = match_avg["Senior"].round(2)
junior_avg = match_avg["Junior"].round(2)

percent_avg = (((senior_avg - junior_avg)/senior_avg)*100).round(2)
print(f"{senior_avg} % {junior_avg} = {percent_avg}")
"""             867.78 % 440.62 = 49.22 """






