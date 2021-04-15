from math import exp
from library.errors.scalars import two_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.rounding import rounded_value

def logarithmic_roots(first_constant, second_constant, precision = 4):
    """
    Calculates the roots of a logarithmic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the logarithmic term of the original logarithmic function
    second_constant : int or float
        Coefficient of the constant term of the original logarithmic function
    precision : int, default=4
        Maximum number of digits that can appear after the decimal place of the resultant roots

    Raises
    ------
    TypeError
        First two arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    roots : list
        List of the x-coordinates of all of the x-intercepts of the original function

    See Also
    --------
    :func:`~library.analyses.equations.logarithmic.logarithmic_equation`, :func:`~library.analyses.derivatives.logarithmic.logarithmic_derivatives`, :func:`~library.analyses.integrals.logarithmic.logarithmic_integral`, :func:`~library.models.logarithmic.logarithmic_model`

    Notes
    -----
    - Standard form of a logarithmic function: :math:`f(x) = a\\cdot{\\ln{x}} + b`
    - Logarithmic formula: :math:`x = \\text{e}^{-\\frac{b}{a}}`

    Examples
    --------
    Calculate the roots of a logarithmic function with coefficients 2 and 3
        >>> roots1 = logarithmic_roots(2, 3)
        >>> print(roots1)
        [0.2231]
    Calculate the roots of a logarithmic function with coefficients 5 and -7
        >>> roots2 = logarithmic_roots(5, -7)
        >>> print(roots2)
        [4.0552]
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant], precision)
    
    # Create root
    root = exp(-1 * coefficients[1] / coefficients[0])

    # Round root
    result = [rounded_value(root, precision)]
    return result

def logarithmic_roots_first_derivative(first_constant, second_constant, precision = 4):
    root = [None]
    return root

def logarithmic_roots_second_derivative(first_constant, second_constant, precision = 4):
    root = [None]
    return root