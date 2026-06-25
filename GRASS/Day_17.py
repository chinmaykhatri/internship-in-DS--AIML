import pandas as pd
df = pd.read_json("student-data.json")
pd.DataFrame(df)
""" Sorting
    1. df.sort_values("column_name") -> Sort by Single Column
    2. df.sort_values("Age", ascending=True) -> Sort in Ascending Order
    3. df.sort_values("Age", ascending=False) -> Sort in Descending Order
    4. df.sort_values(["col1", "col2"]) -> Sort Multiple Columns
    5. df.sort_values( ["Age", "Salary"], ascending=[True, False] ) -> Multiple Columns with Descending Order
"""
# by default ascending
# df.sort_values("english")
 
# decending
# df.sort_values("english",ascending=False)
 
# by default ascending method 1
# df.sort_values(by=['english'],ascending=[False])
 
# multiple cols sort
# df.sort_values(by=['english','maths'],ascending=[False ,True])

# a to z
# df['name'] = df['name'].str.lower()

# A to Z
# df["name"] = df["name"].str.upper()
# print(df.sort_values('name'))

# add column total = py+math+english
# df["Total"] = df["physics"] + df["english"] + df["maths"]
# print(df.sort_values("Total"))

# add row
# df.loc[14] = ["harsh","male",99,97,98,294]
# print(df)

# update column
# df.rename(columns= {"Total":"Total marks"},inplace= True)
# print(df)

#update row
# df.loc[10,["name","gender"]] = ['harsh','male']
# print(df)

# delete row 
# df.drop(14, axis= 0 , inplace=True)
# print(df)

# delete column
# df.drop("Total marks", axis= 1, inplace= True)
# print(df)
 
# df.drop(df.index[1:4], inplace=True)

# print(df)

# df.drop([6,7,8,9,10,11,12,13],inplace=True)
# print(df)
# df['doj'] = ['2025-01-01','2025-02-02','2025-03-03','2025-04-04','2025-05-05','2025-06-06']
# print(df)
# print(df['doj'].dtype)

# convert string to date
# df['doj'] = pd.to_datetime(df['doj'])
# print(df['doj'].dtype)

# date operation
# print(df['doj'].dt.year)
# print(df['doj'].dt.month)
# print(df['doj'].dt.day)
# print(df['doj'].dt.day_name())

# 20 days
# print(df['doj'] + pd.to_timedelta(20, unit = 'D'))
# print(df['doj'] + pd.to_timedelta("20 days"))
for i in range(5):
    print(i)