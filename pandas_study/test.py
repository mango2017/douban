import numpy as np
import pandas as pd
# print(pd.__version__)

mylist = list('abc')
myarr = np.arange(3)
mydict = dict(zip(mylist,myarr))
print(mylist)
print(myarr)
print(mydict)

ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
# print("{}\n{}\n{}\n".format(my))

