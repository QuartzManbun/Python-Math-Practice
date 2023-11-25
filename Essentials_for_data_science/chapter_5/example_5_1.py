import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# import points
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")


# extract input variables (all rows, all columns but last column
X = df.values[:, :-1]

# extract output column (all rows, last column)
Y = df.values[:, -1]


# fit a line to the points
fit = LinearRegression().fit(X,Y)

m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

plt.plot(X, Y, 'o')
plt.plot(X, m*X+b)
plt.show()

