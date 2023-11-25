import pandas as pd
from numpy.linalg import  inv
import numpy as np 

# import points 

df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")


# extract vinput variables (all rows, all colums but last colum)  
X = df.values[:, :-1].flatten()

# extract placeholder "1" column to generate intercept 
X_1 = np.vstack([X, np.ones(len(X))]).T

# extract output column (all rows, last column)
Y = df.values[:, -1]

# calculate coefficients for slope and intercept 
b = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)
print(b) 
