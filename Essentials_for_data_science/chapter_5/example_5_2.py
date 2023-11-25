import pandas as pd

# import points
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ",").itertuples()



# test with a given line 
m = 1.93939
b = 4.73333

# calculate the residuals 

for p in points:
    y_actual = p.y
    y_predict = m*p.x + b  
    residual = y_actual - y_predict
    print(residual)

