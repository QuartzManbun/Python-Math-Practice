from numpy import array 

# declare i-hat and J-hat 
# i_hat = array([2,0])
# j_hat = array([0,3])

# # compose basis matrix using i-hat and j-hat 
# # also need to transpose rows into columns 
# basis = array([i_hat,j_hat]).transpose()

# # declare vector v 
# v = array([1,1])

# # create new vector with .dot()
# new_v = basis.dot(v)

# print(new_v)

i_hat = array([2,0])
j_hat = array([0,3])

# compsoe basis matrix using i-hat and jhat 
# also need to transpose rose to columns

basis = array([i_hat, j_hat]).transpose()

# declare the vector v 

v = array([2,1])

# create new vector 
# by transforming v with dot product
new_v = basis.dot(v)

print(new_v)