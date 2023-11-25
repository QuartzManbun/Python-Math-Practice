import pandas as pd

# import points 
points = pd.read_csv("https://bit.ly/2KF29Bd").itertuples()

# test with a given line 
m = 1.93939
b = 4.73333

sum_of_squares = 0.0

# calculate sume of squares 
for p in points: 
    y_actual = p.y
    y_predict = m*p.x + b 
    residual_squared = (y_predict - y_actual)**2
    sum_of_squares += residual_squared

print("sum of squares = {}".format(sum_of_squares))