from math import sin, cos, atan2
from .error import error
from matrices.multiplication import multiplication
from matrices.transpose import transpose
from matrices.inverse import inverse

def sinusoidal(data):
    independent_matrix = []
    dependent_matrix = []
    for i in range(len(data)):
        independent_matrix.append([
            1,
            data[i][0],
            data[i][0]**2,
            data[i][0]**3,
            data[i][0]**4,
            data[i][0]**5,
            data[i][0]**6,
            data[i][0]**7,
            data[i][0]**8,
            data[i][0]**9
        ])
        dependent_matrix.append([data[i][1]])
        print(f'SINUSOIDAL Independent Matrix: {independent_matrix}')
        print(f'SINUSOIDAL Dependent Matrix: {dependent_matrix}')
    transposition = transpose(independent_matrix)
    print(f'SINUSOIDAL Transposition: {transposition}')
    product = multiplication(transposition, independent_matrix)
    print(f'SINUSOIDAL Product: {product}')
    inversion = inverse(product)
    print(f'SINUSOIDAL Inversion: {inversion}')
    second_product = multiplication(inversion, transposition)
    print(f'SINUSOIDAL Second Product: {second_product}')
    solution = multiplication(second_product, dependent_matrix)
    print(f'SINUSOIDAL Solution: {solution}')
    constant_b = (120 * solution[5][0] / solution[1][0])**(1/4)
    constant_c = atan2((-2 * solution[2][0]), (constant_b * solution[1][0]))
    constant_a = solution[1][0] / (constant_b * cos(constant_c))
    constant_d = solution[0][0] - (constant_a * sin(constant_c))
    constants = [
        [constant_a],
        [constant_b],
        [constant_c],
        [constant_d]
    ]
    print(f'SINUSOIDAL Constants: {constants}')
    equation = lambda x: constants[0][0] * sin(constants[1][0]*x + constants[2][0]) + constants[3][0]
    inaccuracy = error(data, equation)
    result = {
        'constants': solution,
        'error': inaccuracy
    }
    return result