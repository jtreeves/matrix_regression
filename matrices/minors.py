from .determinant import determinant

def diminished(matrix, row, column):
    print(f'matrix: {matrix}')
    print(f'row: {row}')
    print(f'column: {column}')
    result = []
    length = len(matrix) - 1
    for i in range(length):
        print(f'i: {i}')
        result.append([])
        print(f'result initial: {result}')
        for m in range(len(matrix)):
            print(f'm before if: {m}')
            for n in range(len(matrix[0])):
                print(f'n before if: {n}')
                if m != row and n!= column:
                    print(f'm after if: {m}')
                    print(f'n after if: {n}')
                    result[i].append(matrix[m][n])
                    print(f'result final: {result}')
    return result

def minors(matrix):
    r1c1 = determinant([[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]])
    r1c2 = determinant([[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]])
    r1c3 = determinant([[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]])
    r2c1 = determinant([[matrix[0][1], matrix[0][2]], [matrix[2][1], matrix[2][2]]])
    r2c2 = determinant([[matrix[0][0], matrix[0][2]], [matrix[2][0], matrix[2][2]]])
    r2c3 = determinant([[matrix[0][0], matrix[0][1]], [matrix[2][0], matrix[2][1]]])
    r3c1 = determinant([[matrix[0][1], matrix[0][2]], [matrix[1][1], matrix[1][2]]])
    r3c2 = determinant([[matrix[0][0], matrix[0][2]], [matrix[1][0], matrix[1][2]]])
    r3c3 = determinant([[matrix[0][0], matrix[0][1]], [matrix[1][0], matrix[1][1]]])
    result = [
        [r1c1, r1c2, r1c3],
        [r2c1, r2c2, r2c3],
        [r3c1, r3c2, r3c3]
    ]
    return result

def minors_all(matrix):
    result = []
    return result