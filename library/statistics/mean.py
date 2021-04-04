from library.errors.vectors import vector_of_scalars
from .summation import sum_value

def mean_value(data):
    """
    Determines the arithmetic mean of a data set

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list or tuple
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    mean : int or float
        Arithmetic mean of the data set

    Examples
    --------
    Determine the mean of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> mean_even = mean_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1])
        >>> print(mean_even)
        30.9
    Determine the mean of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> mean_odd = mean_value([12, 81, 13, 8, 42, 72, 91, 20, 20])
        >>> print(mean_odd)
        39.888888888888886
    """
    vector_of_scalars(data, 'only')
    result = sum_value(data) / len(data)
    return result