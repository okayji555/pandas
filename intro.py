import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

var = pd.DataFrame(mydataset)

print(var)


#for version check
print(pd.__version__)
