import pandas as pd 

# import points from CSV 
points = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())

# building the model 
m = 0.0 
b = 0.0

#the learnign rate 
L = .001 

# the number of iterations 


iterations = 100_000

#  number of elements in X 

n = float(len(points))
# perform gradient descent 
for i in range(iterations): 

    # slope with respect ot m 
    D_m = sum(2 * p.x * ((m*p.x + b) -p.y) for p in points)

    # sloep with respect obe 
    D_b = sum(2*((m*p.x + b) - p.y) for p in points )

    # update m and b   
    m-= L * D_m
    b -= L *D_b

print("y ={0}x + {1}".format(m,b))
