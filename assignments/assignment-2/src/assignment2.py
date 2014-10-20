# This is the code used for the second mandatory assignment in
# MAT1120 - Linear Algebra
# at the University of Oslo.

import numpy as np

def is_orthogonal(matrix):
    """ Tests whether a matrix is semi-orthogonal
        based on the definition given in the
        assignment text
        
        Assumes a square matrix (n x n), 
        raises an exception if not square.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise Exception('Matrix is not square')

    B = matrix.T.dot(matrix) # Forms the matrix to be tested
    eps = 1.0e-12
    B[np.abs(B) < eps] = 0 # Makes all entries below a certain threshold zero
    B = B.getA()
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if i == j:
                if  B[i][j] <= 0:
                    return False
            else:
                if abs(B[i][j]) > eps:
                    return False
    return True

def find_inverse(matrix):
    """ Finds and returns the inverse of a matrix with the properties
    given in the assignment text.
    
    Assumes a semi-orthagonal matrix,
    raises an exception if the matrix
    is not orthogonal.
    """
    if not is_orthogonal(matrix):
        raise Exception("Matrix is not orthogonal")
    
    
    matrix_inv = np.zeros((matrix.shape[0], matrix.shape[0])) 
    index = 0
    for i in matrix.T: # Iterating over columns instead of rows, hence the transpose
        matrix_inv[index] = transform_vector(i)
        index += 1
    
    eps = 1.0e-12
    matrix_inv[np.abs(matrix_inv) < eps] = 0
    return matrix_inv

def transform_vector(vec):
    """ Transforms the given vector u_j into
    u_j' as given in problem 1
    """
    vec = vec.getA()
    return (1./vec.dot(vec.T))*vec

if __name__ == "__main__":
    
    t1 = np.pi / 6; t2 = np.pi / 2; t3 = 5 * np.pi / 6
    A = np.matrix([[1, np.cos(t1), np.cos(2*t1)],[1,np.cos(t2), np.cos(2*t2)], [1, np.cos(t3), np.cos(2*t3)]])
    B = np.matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
