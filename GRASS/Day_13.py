#------pandas------
""" What is Pandas?
    Pandas is a Python library used for:
    1. Reading data
    2. Cleaning data
    3. Analyzing data 
    4. Munipulating data  
"""
import pandas as pd

# list
# df = pd.Series([10,20,30])
# print(df)

# dict
# dict = {"name":["dheeraj","harsh","anjali","praveen","kunal"],
#         "age":[20,21,22,23,24],
#         "Salary":[{"In-hand":"15000","ctc":"1.2 lpa"}, {"In-hand":"20000","ctc":"2.2 lpa"},
#                   {"In-hand":"25000","ctc":"3.1 lpa"},{"In-hand":"30000","ctc":"3.2 lpa"},
#                   {"In-hand":"40000","ctc":"4.2"}]
#         }
# df = pd.DataFrame(dict)
# print(df)

"""What is DataFrame()?
-> A DataFrame is a two-dimensional labeled data structure in Pandas that organizes data into 
   rows and columns and allows efficient data analysis and manipulation.
   
   Difference between CSV(Comma Separated Values), JSON(JavaScript Object Notation), and Excel 
|    Feature      | CSV            | JSON            | Excel            |
| syntax          | .csv           | .json           | .xlsx            |
| Format          | Plain text     | Key-value pairs | Spreadsheet      |
| Human readable  | Yes            | Yes             | Through Excel    |
| Multiple sheets | No             | No              | Yes              |
| File size       | Small          | Medium          | Larger           |
| Common use      | Data exchange  | APIs/Web apps   | Business reports |
| Import          | pd.read_csv(fn)| pd.read_json(fn)| pd.read_excel(fn)|
   """

df = pd.read_csv("file2.csv")
print(df)

df1 = pd.read_excel("file2.xlsx")
print(df1)

df2 = pd.read_json("file2.json")
print(df2)