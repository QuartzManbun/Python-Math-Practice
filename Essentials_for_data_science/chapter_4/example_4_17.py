from sympy import * 

# 4x + 2y + 4z = 44
# 5x + 3y + 4z = 56
# 9x + 3y + 6z = 72

A = Matrix([
    [4, 2, 4],
    [5 ,3, 7],
    [9, 3, 6]
])

# dot product between a and its inverse 
# will produce identy function 
inverse = A.inv()
identy = inverse * A
print("INVERSE: {}".format(inverse))

print("IDENTITY: {}".format(identy))

