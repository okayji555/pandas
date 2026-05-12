import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)
var = pd.Series(a, index = ["x","y","z"])

print(myvar)
print(var)
print(var["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}

cal = pd.Series(calories)

print(cal)
