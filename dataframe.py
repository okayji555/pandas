import pandas as pd

data = {
    "calories": [420, 350, 534],
    "time": [35, 20, 40]
}

df = pd.DataFrame(data)

print(df,"\n")
print(df.loc[0], "\n")    # loc specifies the rows
print(df.loc[[0,1]], "\n")


newdf = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(newdf, "\n")
print(newdf.loc["day2"])