import random

def f(x):
    return (x-3)**2 + 4 

def dx_f(x):
    return 2*(x-3) 

# the learnng rate 
L = .001 

# the number of iterations to perform gradient descent 
iterations = 100_000

# start at a random X 
x = random.randint(-15,15); 

for i in range(iterations): 

    # get slope/
    d_x = dx_f(x) 
    x -= L * d_x

print(x, f(x))
