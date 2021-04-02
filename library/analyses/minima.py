from library.errors.vectors import multitype_vector

def minima_points(intervals):
    """
    Calculates the minima of a specific function

    Parameters
    ----------
    intervals : list or tuple
        Array containing the sign chart of the specific function's first derivative

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    ValueError
        First element of argument must be either 'constant', 'positive', or 'negative'
    TypeError
        Second element of argument must be an integer or a float

    Returns
    -------
    points : list
        Values of the x-coordinates at which the original function has a relative minimum; if the function has no minima, then it will return a list of `None`

    Examples
    --------
    Generate the derivatives of a cubic function with coefficients 1, -15, 63, and -7
        >>> test1 = cubic_derivatives(1, -15, 63, -7)
    Calulate the critical points of the first derivative of that function (and round the results to four decimal places)
        >>> test2 = critical_points('cubic', 1, [-1, -15, 63, -7], 4)
    Create the sign chart of that derivative
        >>> test3 = sign_chart(test1['first']['evaluation'], test2)
    Calculate the minima of the original cubic function
        >>> test4 = minima_points(test3)
    Print the x-coordinates of the original cubic function's minima
        >>> print(test4)
        [7.0]
    """
    multitype_vector(intervals)
    result = []
    for i in range(len(intervals)):
        try:
            if intervals[i] == 'negative' and intervals[i + 2] == 'positive':
                result.append(intervals[i + 1])
        except IndexError:
            pass
    if len(result) == 0:
        result.append(None)
    return result