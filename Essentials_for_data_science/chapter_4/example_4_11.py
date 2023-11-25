from numpy import array 

# transformation 1 

i_hat1 = array([0,1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# transformation 2 
i_hat2 = array([1,0])
j_hat2 = array([1,1])
transform2 = array([i_hat2, j_hat2]).transpose()

# combine transformation 
combined = transform2 @ transform1
# test 
print("combined matrix:\n {}".format(combined))

v= array([1,2])
print(combined.dot(v))

0
