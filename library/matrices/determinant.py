from library.errors.matrices import square_matrix
from library.errors.scalars import whole_number

def inner_determinant(matrix, row, column):
    square_matrix(matrix)
    whole_number(row, 'second')
    whole_number(column, 'third')
    result = []
    storage = {}
    for m in range(len(matrix)):
        if m != row:
            storage[m] = []
            for n in range(len(matrix[0])):
                if n!= column:
                    storage[m].append(matrix[m][n])
    for key in storage:
        result.append(storage[key])
    return result

def linear_determinant(matrix, result = 0):
    """
    Calculate the determinant of a matrix

    Parameters
    ----------
    matrix : list
        List of lists of numbers representing a matrix

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list
    TypeError
        Elements nested within first argument must be integers or floats
    ValueError
        First argument must contain the same amount of lists as the amount of elements contained within its first list
    
    Returns
    -------
    determinant : float
        Determinant of a matrix

    See Also
    --------
    :func:`~library.matrices.minors.matrix_of_minors`, :func:`~library.matrices.inverse.inverse_matrix`

    Notes
    -----
    - Original matrix: :math:`\\mathbf{A} = \\begin{bmatrix} a_{1,1} & a_{1,2} & \\cdots & a_{1,j} & a_{1,n} \\\\ a_{2,1} & a_{2,2} & \\cdots & a_{2,j} & a_{2,n} \\\\ a_{i,1} & a_{i,2} & \\cdots & a_{i,j} & a_{i,n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m,1} & a_{m,2} & \\cdots & a_{m,j} & a_{m,n} \\end{bmatrix}`
    - Determinant of matrix (if :math:`\\mathbf{A}` contains an odd number of columns): :math:`|\\mathbf{A}| = a_{1,1}\\cdot{|\\mathbf{A}_{1,1}|} - a_{1,2}\\cdot{|\\mathbf{A}_{1,2}|} + \\cdots - a_{1,j}\\cdot{|\\mathbf{A}_{1,j}|} + a_{1,n}\\cdot{|\\mathbf{A}_{1,n}|}`
    - Determinant of matrix (if :math:`\\mathbf{A}` contains an even number of columns): :math:`|\\mathbf{A}| = a_{1,1}\\cdot{|\\mathbf{A}_{1,1}|} - a_{1,2}\\cdot{|\\mathbf{A}_{1,2}|} + \\cdots + a_{1,j}\\cdot{|\\mathbf{A}_{1,j}|} - a_{1,n}\\cdot{|\\mathbf{A}_{1,n}|}`
    - |determinant|

    Examples
    --------
    Calculate the determinant of [[1, 2], [3, 4]]
        >>> determinant_2x2 = linear_determinant([[1, 2], [3, 4]])
        >>> print(determinant_2x2)
        -2
    Calculate the determinant of [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
        >>> determinant_3x3 = linear_determinant([[2, 3, 5], [7, 11, 13], [17, 19, 23]])
        >>> print(determinant_3x3)
        -78
    """
    square_matrix(matrix)
    whole_number(result, 'second')
    if len(matrix) == 1:
        result += matrix[0][0]
        return result
    else:
        alternating = []
        minors = []
        leads = matrix[0]
        for i in range(len(leads)):
            minors.append(inner_determinant(matrix, 0, i))
            if i % 2 == 0:
                alternating.append(leads[i])
            else:
                alternating.append(-1 * leads[i])
        for j in range(len(alternating)):
            result += alternating[j] * linear_determinant(minors[j])
    return float(result)