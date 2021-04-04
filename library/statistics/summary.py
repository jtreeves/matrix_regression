from library.errors.vectors import vector_of_scalars
from library.errors.scalars import positive_integer
from .minimum import minimum_value
from .maximum import maximum_value
from .median import median_value
from .quartiles import quartile_value
from .rounding import rounded_value

def five_number_summary(data, precision):
    """
    Calculates the five number summary of a given data set: minimum, first quartile, median, third quartile, and maximum

    Parameters
    ----------
    data : list or tuple
        List of numbers to analyze
    precision : int
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    TypeError
        First argument must be a 1-dimensional list or tuple
    TypeError
        Elements of first argument must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    summary['minimum'] : int or float
        Smallest value from the data set
    summary['q1'] : int or float
        First quartile of the data set, below which 25% of the data fall
    summary['median'] : int or float
        Middle value of the data set, splitting the data evenly in half
    summary['q3'] : int or float
        Third quartile of the data set, above which 25% of the data fall
    summary['maximum'] : int or float
        Largest value from the data set

    Examples
    --------
    Determine the five number summary of the set [21, 53, 3, 68, 43, 9, 72, 19, 20, 1] (and round the result to two decimal places)
        >>> summary_even = five_number_summary([21, 53, 3, 68, 43, 9, 72, 19, 20, 1], 2)
        >>> print(summary_even['q1'])
        9
        >>> print(summary_even['maximum'])
        72
    Determine the five number summary of the set [12, 81, 13, 8, 42, 72, 91, 20, 20] (and round the result to two decimal places)
        >>> summary_odd = five_number_summary([12, 81, 13, 8, 42, 72, 91, 20, 20], 2)
        >>> print(summary_odd['q3'])
        76.5
        >>> print(summary_odd['minimum'])
        8
    """
    vector_of_scalars(data, 'first')
    positive_integer(precision)
    min_value = minimum_value(data)
    rounded_min = rounded_value(min_value, precision)
    max_value = maximum_value(data)
    rounded_max = rounded_value(max_value, precision)
    q1 = quartile_value(data, 1)
    rounded_q1 = rounded_value(q1, precision)
    q3 = quartile_value(data, 3)
    rounded_q3 = rounded_value(q3, precision)
    median = median_value(data)
    rounded_med = rounded_value(median, precision)
    result = {
        'minimum': rounded_min,
        'q1': rounded_q1,
        'median': rounded_med,
        'q3': rounded_q3,
        'maximum': rounded_max
    }
    return result