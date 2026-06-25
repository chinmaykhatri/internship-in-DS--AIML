import pandas as pd
# d= { 
#     "name": ["vishal","virat","vineet"],
#     "salary": [100,200,300]
#     }
# df = pd.DataFrame(data=d)
# add columns
# df["holidays"] = df["salary"]/100
# df["decrement"] = [10,20,30]
# delete column
# df.drop(["salary","name"],axis= 1,inplace= True)
# print(df)

""" Operation on Rows
    1.  print(df.loc[row,"col name"]) -> label based (get single value)
    2.  print(df.loc[row]) -> label based (get complete row)
    3.  print(df.loc[[0, 2]]) -> get multiple rows
    4.  print(df.loc[[0, 2], ["col1", "col2"]]) multi rows and cols
    5.  print(df.iloc[row_position, column_position])
    6.  print(df.iloc[row_position])
    7.  print(df.iloc[[row1, row2]])
    8.  print(df.iloc[[row1, row2], [col1, col2]])
    9.  print(df.iloc[[0, 2], [0]])
    10. print(df.iloc[1, [0, 2]])
    11. print(df.iloc[0:3])
"""

# d= { 
#     "name": ["vishal","virat","vineet"],
#     "salary": [100,200,300]
#     }
# df = pd.DataFrame(data=d)
# print(df.loc[2,"name"])
# print(df.iloc[2,0])
# get single row data 
# print(df.iloc[1]) # get single row data using iloc 
# print(df.loc[1])  # get single row data using loc

# get multi rows using iloc
# print(df.iloc[0:3])
# get multi rows using loc
# print(df.loc[0:3])

# sub data get
# df1 = df.iloc[0:2,[0]] # using iloc
# print(df1)
# df2 = df.loc[1:2,["name"]] # using loc
# print(df2)

# example
# data = {
#     "Emp_ID": [101,102,103,104,105,106],
#     "Name": ["Amit","Riya","Raj","Sara","John","Neha"],
#     "Department": ["IT","HR","Finance","IT","Sales","HR"],
#     "Salary":[50000,45000,60000,55000,48000,52000],
#     "Experience":[2,3,5,4,1,3]
# }
# df = pd.DataFrame(data)
# df.set_index("Emp_ID",inplace= True)
# print(df.loc[1])
# print(df.iloc[1])
# print(df.loc[0:3])
# print(df.iloc[0:4])
# print(df.loc[0:4,["Emp_ID","Name"]])
# print(df.iloc[0:4,[0,1]])
# print(df.loc[101])
# print(df.iloc[0])

# question
# df = pd.read_json("student-data.json")
# male_data = df.loc[df["gender"] == "Male"]

# print(male_data)
# print(df.iloc[3:9:5])

"""
Filter DataFrame

Filter DataFrame -> Ex. df[df["col name"] > 22]
Filter Using Greater Than (>)
df[df["column"] > value]
Filter Using Less Than (<)
df[df["column"] < 22]
Filter Using Equal To (==)
df[df["column"] == 22]
Filter Using Not Equal To (!=)
df[df["Age"] != 22]
Filter String Columns
df[df["column"] == "Sara"]
Multiple Conditions (AND)
df[(df["col1"] > 22) & (df["col2"] > 55000)]
Multiple Conditions (OR)
df[(df["col1"] > 23) | (df["col2"] > 55000)]
Using query()
df.query("col1 > 22")
"""
df = pd.read_json("student-data.json")
# filter-1 -> english values equal to 95
# print(df[df["english"] == 95])

# filter-2 -> maths values less than 60
# print(df[df["maths"] < 60])

# filter-3 -> physics values less than and equal to 56
# print(df[df["physics"]<= 56])

# filter for multiple condition -> df[(condition-1) & (condition-2)]
print(df[(df["english"]>90) & (df["maths"]>90)])
# for only names 
print(df[(df["english"]>90) & (df["maths"]>90)]["name"])
print(df[(df["english"]>90) & (df["maths"]>90) & (df["gender"] == "male")]["name"])