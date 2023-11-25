import pandas as pd 
import numpy as np

# input data 
data = pd.read_csv('https://bit.ly/2KF29Bd', header = 0)

X = data.iloc[ :, 0].values
Y = data.iloc[:,1].values

n = data.shape[0] 

# building the model 
m = 0.0 
b = 0.0 

sample_size = 1 
L = .0001 
epochs = 1_000_000 

# performing stochastic gradient decent 
for i in range(epochs):
    idx = np.random.choice(n, sample_size, replace = False)
    x_sample = X[idx]
    y_sample = Y[idx]

    # the current predicted value of Y 
    Y_pred = m * x_sample + b 

    # d/dm derivative of loss function 
    D_m =(-2 / sample_size) * sum(x_sample * (y_sample - Y_pred))

    # d/db derivative of loss function 
    D_b = (-2/ sample_size) * sum(y_sample - Y_pred)

    m = m - L * D_m 
    b = b - L * D_b 

    if i % 10000 == 0:
        print( i, m, b)
    
print("y = {0}x + {1}".format(m,b))
