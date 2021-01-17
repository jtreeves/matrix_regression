from .determinant import determinant

def minors(matrix):
    r1c1 = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    r1c2 = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    r1c3 = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    r2c1 = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    r2c2 = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    r2c3 = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    r3c1 = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    r3c2 = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    r3c3 = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    result = [
        [r1c1, r1c2, r1c3],
        [r2c1, r2c2, r2c3],
        [r3c1, r3c2, r3c3]
    ]
    return result