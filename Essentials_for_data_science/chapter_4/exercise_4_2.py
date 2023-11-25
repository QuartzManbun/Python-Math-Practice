from numpy import array

# define i_hat and j_hat
i_hat = array([-2,1])
j_hat = array([1,-2])

basis = array([i_hat, j_hat]).transpose()

v = array([1,2])

new_v = basis.dot(v)
print(new_v)
