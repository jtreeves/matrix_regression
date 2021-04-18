from library.errors.scalars import two_scalars, positive_integer
from library.statistics.sort import sorted_list
from library.statistics.rounding import rounded_value, rounded_list

def generate_elements(initial_value, periodic_unit, precision = 4):
    """
    Generates a vector containing an initial numerical value, four additional numerical values created by incrementing the initial value by a periodic unit four times, and a string value for the general form of all values in the vector, made up of a multiple of the periodic unit added to the initial value

    Parameters
    ----------
    initial_value : int, float
        Starting value to adjust to fit into a range
    periodic_unit : int, float
        Unit by which the initial value should be incrementally increased or decreased to fit into a range
    precision : int, default=4
        Upper bound of range into which the initial value must be adjusted (final value should be less than or equal to maximum)

    Raises
    ------
    TypeError
        First and second arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    generated_vector : list
        Vector containing five numerical values, each a set incremenent apart from one another, and a string value representing the general form of all numerical elements in the vector as well as any additional numerical elements that could be generated from it in the future

    See Also
    --------
    :func:`~library.statistics.ranges.shift_into_range`, :func:`~library.analyses.points.shifted_points_within_range`, :func:`~library.analyses.roots.sinusoidal.sinusoidal_roots`

    Notes
    -----
    - Initial value: :math:`v_i`
    - Periodic unit: :math:`\\lambda`
    - Set of all values derived from initial value and periodic unit: :math:`g = \\{ v \\mid v = v_i + \\lambda\\cdot{k} \\}`

        - :math:`k \\in \\mathbb{Z}`

    Examples
    --------
    Generate a vector of elements based off an initial value of 3 and a periodic unit of 2
        >>> generated_vector_int = generate_elements(3, 2)
        >>> print(generated_vector_int)
        [3.0, 5.0, 7.0, 9.0, 11.0, '3.0 + 2.0k']
    Generate a vector of elements based off an initial value of 17.23 and a periodic unit of 5.89
        >>> generated_vector_float = generate_elements(17.23, 5.89)
        >>> print(generated_vector_float)
        [17.23, 23.12, 29.01, 34.9, 40.79, '17.23 + 5.89k']
    """
    # Handle input errors
    two_scalars(initial_value, periodic_unit)
    positive_integer(precision)

    # Generate values from inputs
    first_value = initial_value + 1 * periodic_unit
    second_value = initial_value + 2 * periodic_unit
    third_value = initial_value + 3 * periodic_unit
    fourth_value = initial_value + 4 * periodic_unit

    # Store values in list
    values = [initial_value, first_value, second_value, third_value, fourth_value]

    # Sort values
    sorted_values = sorted_list(values)

    # Round values
    rounded_values = rounded_list(sorted_values, precision)

    # Create general form
    rounded_periodic_unit = rounded_value(periodic_unit, precision)
    rounded_initial_value = rounded_value(initial_value, precision)
    general_form = str(rounded_initial_value) + ' + ' + str(rounded_periodic_unit) + 'k'

    # Store numerical values and general form in single list
    results = [*rounded_values, general_form]
    return results