from numpy import array 

# declare i-hat and j-hat 
i_hat = array([2,3])
j_hat = array([2,-1])

# compose a basis vector fomr i_hat and j_hat
basis = array([i_hat, j_hat]).transpose()

# declare vector v 0
v = array([1,2])

# create new vector  
# by transforming v with dot produt 
new_v = basis.dot(v)


print(new_v) 


