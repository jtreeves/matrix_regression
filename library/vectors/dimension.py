from library.errors.matrices import matrix_of_scalars, level
from library.errors.scalars import positive_integer

def single_dimension(matrix, scalar):
    """
    Extracts a column vector as a row vector from a matrix according to an integer corresponding to the column's position

    Parameters
    ----------
    matrix : list or tuple
        List containing other lists, where each inner list is a row and elements within those inner lists correspond to columns
    scalar : int
        Number corresponding to the column's position

    Raises
    ------
    TypeError
        First argument must be a 2-dimensional list or tuple
    TypeError
        Elements nested within the first argument's lists must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    vector : list
        List containing only integers or floats

    See Also
    --------
    :func:`~library.vectors.column.column_conversion`

    Notes
    -----
    - Matrix: :math:`\\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\\ \\cdots & \\cdots & \\cdots & \\cdots \\\\ a_{m1} & a_{m2} & \\cdots & a_{mn} \\end{bmatrix}`
    - Row vector corresponding to the :math:`n`\ th column of the matrix: :math:`\\langle a_{1n}, a_{2n}, \\cdots, a_{mn} \\rangle`

    Examples
    --------
    Extract the second column from the matrix [[3, 5, 9], [1, -4, 2]]
        >>> vector_2c = single_dimension([[3, 5, 9], [1, -4, 2]], 2)
        >>> print(vector_2c)
        [5, -4]
    Extract the first column from the matrix [[3, 5, 9], [1, -4, 2]]
        >>> vector_1c = single_dimension([[3, 5, 9], [1, -4, 2]], 1)
        >>> print(vector_1c)
        [3, 1]
    """
    matrix_of_scalars(matrix, 'first')
    positive_integer(scalar)
    level(matrix, scalar)
    result = []
    for element in matrix:
        result.append(element[scalar - 1])
    return result