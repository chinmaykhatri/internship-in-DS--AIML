import pandas as pd
df = pd.read_json("file2.json")
# print(df)

""" Basic Dataframe Understanding
    1. head()
    2. tail()
    3. shape
    4. info()
    5. rename
    6. describe() -> count,mean,std,min,max
"""

# head -> Starting 5 rows
# print(df.head())

# head -> starting 2 rows data show
# print(df.head(2))

# print(df.head(-2)) # excluding last 2 rows data and remaining shows

# tail()
# print(df.tail())
# print(df.tail(3))
# print(df.tail(-3))

# shape -> It is used for identify no of column and rows in 2d & only rows in series
# print(df.shape) # rows -> 5 and column -> 3
# df.info()
""" What is verbose in pandas?
    In Pandas, verbose is a parameter used in some functions to display extra information/details 
    about the operation being performed.
        verbose=True → More details.
        verbose=False → Less details / summary only.
"""

# rename
# print(df.rename (columns= {"name":" student_name","marks":"salary"},inplace= False))

# print(df.describe())

# example
# data = {
#     "Emp_ID ": [101,102,103,104,105,106],
#     "Name": ["Amit","Riya","Raj","Sara","John","Neha"],
#     "Department": ["IT","HR","Finance","IT","Sales","HR"],
#     "Salary":[50000,45000,60000,55000,48000,52000],
#     "Experience":[2,3,5,4,1,3]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.head(3))
# print(df.head(-2))
# print(df.tail(2))
# print(df.tail(-2))
# print(df.shape)
# df.info()
# print(df.rename(columns={"Experience":"Work_Experience"}))
# print(df.describe())

"""Operation on Columns

    1.  df["column name"] -> selecting column
    2.  df["column name"] = [values] -> add new column
    3.  df.drop("column name",axis=1) -> delete column
    4.  type(df[["column name", "column name"]])
    5.  df.drop(["col1", "col2"], axis=1)
    6.  df[["Name","Salary"]] -> Select Multiple Columns
    7.  df["Bonus"] = values -> Add New Column
    8.  df["Bonus"] = df["Salary"] + 5000 -> Add Calculated Column
    9.  df.drop("Experience", axis=1) -> Delete Single Column
    10. df.drop(["Department","Experience"], axis=1) -> Delete Multiple Columns
    11. df.drop("Department", axis=1, inplace=True) -> Permanent Delete
    12. type(df["Name"]) -> Type of Single Column
    13. type(df[["Name","Salary"]]) -> Type of Multiple Columns
"""

# get single column
# print(df["name"])

# add single column
df["marks"] = [10,20,30,40,50]
df["salary"]= [ 100,200,300,400,500]
df["marks"] = df["salary"] / 2
# print(df)
df["Increment"] = df["salary"]* 1.10
# print(df)

# column name change
df.rename(columns={"Increment":"salary_increment"},inplace= True)
print(df)

""" What is inplace in pandas?
   -> inplace is a parameter that decides whether the original DataFrame/Series 
    should be modified directly or a new modified object should be returned.
   -> inplace=True modifies the original DataFrame or Series directly,
    while inplace=False returns a modified copy and keeps the original data unchanged.
"""