# The code used for problem 3
# in the second mandatory assignment
# in MAT1120 at the University of Oslo

from assignment2 import *
import numpy as np
# Initializing matrices and t values

n = 8
C = np.zeros((n, n))
S = np.zeros((n, n))
t = np.pi/16 + (np.linspace(1, 8, 8)-1)*np.pi/8

for i in range(n):
    for j in range(n):
        C[i][j] = np.cos((j)*t[i])
        S[i][j] = np.sin((j+1)*t[i])

# Verifying that the matrices C and S are semi-orthogonal:

print("Is C semi-orthogonal? " , is_semi_orthogonal(C))
print("Is S semi-orthogonal? " , is_semi_orthogonal(S))

# Finding the inverse matrices of C and S:

print("Inverse of C: ")
print_matrix(C)
print("Inverse of S: ")
print_matrix(S)
