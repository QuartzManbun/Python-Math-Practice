import pandas as pd 
from math import sqrt
# load the data 
points= list(pd.read_csv('https://bit.ly/2KF29Bd',delimiter =",").itertuples())

n = len(points)

# regression line 
m = 1.939
b = 4.733 

# calculate standard error of estimate 
S_e = sqrt((sum((p.y-(m*p.x + b))**2 for p in points))/(n-2))

print(S_e)
