import pandas as pd 
from numpy.linalg import qr, inv 
import numpy as np 

# import points 
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter= ",")

# extrac t input variables, all rose, all colums but the last column)
X = df.values[:, :-1].flatten()

# add placeholder "1" column to generate intercept

X_1 = np.vstack([X, np.ones(len(X))]).transpose()

# extract ouput column(all rows, last column) 

Y = df.values[:, -1]

# calculate coefficients for slope and intercept
# using QR decomposition
Q,R = qr(X_1)

b= inv(R).dot(Q.transpose()).dot(Y) 

print(b) 
