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
print(f"mean differences= {senior_avg} % {junior_avg} = {percent_avg}")
"""             867.78 % 440.62 = 49.22 
"""

# 6) How much more, on average, is the salary of a senior person
# in the software development department compared to a junior person?

salaries_developers = data_frame.groupby("Department")["Salary"].mean()
salaries_juniors = data_frame.groupby("Title")["Salary"].mean()

salary_minus = (salaries_developers["Software Development"] - salaries_juniors["Junior"]).round(2)
print(f"Developers - Juniors= {salary_minus}")
"""             Developers - Juniors= 385.78
"""

#7) How much more salary does a c-level person in the finance department earn on average
# compared to a mid-senior person?

salary_finance = data_frame.loc[data_frame["Department"] == "Finance"].groupby("Title")["Salary"].mean()


print(f"Result(7) = {salary_finance["C-level"]-salary_finance["Mid-Senior"]}")
"""             Result(7) = 240.0
"""

#8) How many times more c-level employees are there in the
# software development department than in the marketing department?

developer_count = (data_frame.loc[data_frame["Department"] == "Software Development"]).groupby("Title")["Salary"].count()
marketing_count = (data_frame.loc[data_frame["Department"] == "Marketing"]).groupby("Department")["Salary"].count()
print(f"Result(8) = {developer_count["C-level"] + marketing_count["Marketing"]}")
"""             Result(8) = 24
"""
