from math import log
from numpy import matrix
from numpy.linalg import inv
from library.statistics.error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

def logarithmic(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([log(data[i][0]), 1])
        dependent_matrix.append([data[i][1]])
    transposition = transpose(independent_matrix)
    product = multiplication(transposition, independent_matrix)
    product_matrix = matrix(product, dtype='float')
    inversion = inv(product_matrix)
    inversion_list = matrix.tolist(inversion)
    second_product = multiplication(inversion_list, transposition)
    solution = multiplication(second_product, dependent_matrix)
    constants = [
        [solution[1][0]],
        [solution[0][0]]
    ]
    equation = lambda x: constants[0][0] + constants[1][0]*log(x)
    inaccuracy = error(data, equation)
    result = {
        'constants': constants,
        'error': inaccuracy
    }
    return result