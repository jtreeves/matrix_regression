from library.errors.vectors import vector_of_scalars
from .maximum import maximum_value
from .minimum import minimum_value

def range_value(data):
    """
    Determines the range of a data set (i.e., the difference between its largest value and its smallest value)

    Parameters
    ----------
    data : list
        List of numbers to analyze

    Raises
    ------
    TypeError
        Argument must be a 1-dimensional list
    TypeError
        Elements of argument must be integers or floats

    Returns
    -------
    interval : float
        Range of data set

    See Also
    --------
    :func:`~library.statistics.sort.sorted_list`, :func:`~library.statistics.minimum.minimum_value`, :func:`~library.statistics.maximum.maximum_value`

    Notes
    -----
    - Set of numbers: :math:`a_i = \\{ a_1, a_2, \\cdots, a_n \\}`
    - Range of set: :math:`R = a_{max} - a_{min}`
    
        - :math:`a_{min} \\leq a_j, \\forall a_j \\in a_i`
        - :math:`a_{max} \\geq a_j, \\forall a_j \\in a_i`

    - |range|

    Examples
    --------
    Determine the range of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1]
        >>> range_even = range_value([21, 53, 3, 68, 43, 9, 72, 19, 20, 1])
        >>> print(range_even)
        71
    Determine the range of the set [12, 81, 13, 8, 42, 72, 91, 20, 20]
        >>> range_odd = range_value([12, 81, 13, 8, 42, 72, 91, 20, 20])
        >>> print(range_odd)
        83
    """
    vector_of_scalars(data, 'only')
    max_value = maximum_value(data)
    min_value = minimum_value(data)
    result = max_value - min_value
    return float(result)