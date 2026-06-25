import pandas as pd 
import numpy as np
df = pd.read_json("file2.json")
pd.DataFrame(df)
"""Handling missing values

    1.  df.isnull() -> Check Missing Values in DataFrame
    2.  df.isnull().sum() -> Count Missing Values in Each Column
    3.  df.isnull().any() -> Check if Any Missing Value Exists
    4.  df.isnull().sum().sum() -> Count Total Missing Values
    5.  df.dropna() -> Remove Rows with Missing Values
    6.  df.dropna(axis=1) -> Remove Columns with Missing Values
    7.  df.fillna(0) | df["Salary"].fillna(0)-> Fill Missing Values with a Fixed Value
    8.  df["Salary"].fillna( df["Salary"].mean() ) -> Fill Missing Values with Mean
    9.  df["Salary"].fillna( df["Salary"].median() ) -> Fill Missing Values with Median
    10. df["Department"].fillna( df["Department"].mode()[0] ) -> Fill Missing Values with Mode
"""
# print(df.isnull())

# example
# df.loc[4,'marks'] = np.nan
# print(df)


# df["marks"] = df["marks"].astype(object)
# df.loc[df["name"] == "anjali", "marks"] = None
# print(df)

# column count missing values
# print(df.isnull().sum())

# url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
# df = pd.read_json(url)
# print(df.isnull())

# drop null values by row
# print(df.dropna())

# drop null values by columns
# print(df.dropna(axis = 1))

# fill by zeros
# print(df.fillna(0))

# filled by hundred
# print(df.fillna(100))

# df.loc[1,'roll no'] = np.nan
# df = df.fillna({"roll no": 200,"marks": 100}, inplace=True)
# print(df)

# df = df["marks"].fillna( df["marks"].mean())
# print(df)

"""Aggregation and group by

    1.  df["Salary"].sum() -> Calculate Sum
    2.  df["Salary"].mean() -> Calculate Average (Mean)
    3.  df["Salary"].max() -> Find Maximum Value
    4.  df["Salary"].min() -> Find Minimum Value
    5.  df["Department"].count() -> Count Values
    6.  df["Department"].value_counts() -> Count Values
    7.  df.groupby("Department")["Salary"].mean() -> Group By and Calculate Mean
    8.  df.groupby("Department")["Salary"].sum() -> Group By and Calculate Sum
    9.  df.groupby( ["Department", "Gender"] )["Salary"].mean() -> Group By Multiple Columns
    10. df.groupby("Department")["Salary"].agg( ["sum", "mean", "max", "min", "count"] ) -> Multiple Aggregations
    11. df.groupby("Department").agg({'col1':'sum','col2':'count'}) -> multiple aggregations
"""

# print(df["marks"].mean())
# print(df["marks"].max())
# print(df["marks"].min())
# print(df["marks"].count())
# print(df["marks"].agg(['sum','mean','min','max']))

"""Concatenate and merge dataframe (joins)

    1. pd.concat([df1,df2],axis=0) -> row joins
    2. pd.concat([df1,df2],axis=1) -> cols joins
    3. pd.merge(df1,df2,how='inner',on='id') -> inner join basis of id
"""
# df1 = pd.read_json("file2.json")
# print(pd.concat([df,df1],axis= 1))
# df1.loc[df1["name"] == "abhishek", "name"] = "harsh"
# print(pd.concat([df,df1],axis= 1))

import matplotlib.pyplot as plt
score = [10,20,30,40]
over = [1,2,3,4]
plt.plot(score, over)
plt.show()
