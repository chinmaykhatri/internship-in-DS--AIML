import pandas as pd

# 1d -> method series
# df = pd.Series([10,20,30])
# print(df)

# example
# d = {"name": "kunal","age": "21","roll-no":"121"}
# df = pd.Series(data = d,index=["name","age","roll-no"])
# print(df)

# Dataframe
d = {"name": ["kunal","dheeraj","anjali","praveen","yash","danish"],
     "age": [12,13,14,15,16,17]
     }
df = pd.DataFrame(data= d)
print(df)