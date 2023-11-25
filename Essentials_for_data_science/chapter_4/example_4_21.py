from numpy import array, diag 
from numpy.linalg import eig, inv


A = array([
    [1,2],
    [4,5]
])

eigenvals, eigenvecs = eig(A)

print("Eigenvalues")
print(eigenvals)
print('\nEigenvectors')
print(eigenvecs)

print("\REBUID MATRIX")
Q = eigenvecs
R = inv(Q)

L = diag(eigenvals)
B= Q @ L @ R 
print(B)
# remember, matrix multiplication is NOT commutitive 


