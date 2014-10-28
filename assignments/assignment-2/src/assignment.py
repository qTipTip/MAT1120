# This is the code used for the second mandatory assignment in
# MAT1120 - Linear Algebra
# at the University of Oslo.

import numpy as np

def is_semi_orthogonal(matrix):
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
    try:
        B = B.getA()
    except:
        pass

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
    if not is_semi_orthogonal(matrix):
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
    try:
        vec = vec.getA()
    except:
        pass
    return (1./vec.dot(vec.T))*vec

def print_matrix(matrix):
    try:
        matrix = matrix.getA()
    except:
        pass
    for i in matrix:
        for j in i:
            print("%7.3f" % (j), end="")
        print()

def matrix_to_tex(matrix, filename):
    outfile = open(filename+".tex", 'w')    
    outfile.write("\\begin{bmatrix}" + "\n")
    body = ""
    for i in matrix:
        for j in i:
            body += "%7.3f" % (j) + "&"
        body = body[:-1]
        body += " \\\\ " + "\n"
    outfile.write(body)
    outfile.write("\end{bmatrix}")

def calc_vector_y(function, n):
    """ Calculates the vector y_o/y_l using a function f_o/f_l, and n midpoints 
        This is used for exercise 8 and 9 
    """
    t = np.pi/16 + (np.linspace(1, 8, 8)-1)*np.pi/8
    return function(t)

if __name__ == "__main__":
    
    t1 = np.pi / 6; t2 = np.pi / 2; t3 = 5 * np.pi / 6
    A = np.matrix([[1, np.cos(t1), np.cos(2*t1)],[1,np.cos(t2), np.cos(2*t2)], [1, np.cos(t3), np.cos(2*t3)]])
    B = np.matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
    print_matrix(find_inverse(A))

    def test_function(t):
        return 2*t

    calc_yo(test_function, 8)
