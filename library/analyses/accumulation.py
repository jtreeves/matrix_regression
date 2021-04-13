from library.errors.scalars import compare_scalars, positive_integer
from library.errors.vectors import vector_of_scalars
from library.errors.analyses import select_equations
from library.analyses.integrals.linear import linear_integral
from library.analyses.integrals.quadratic import quadratic_integral
from library.analyses.integrals.cubic import cubic_integral
from library.analyses.integrals.hyperbolic import hyperbolic_integral
from library.analyses.integrals.exponential import exponential_integral
from library.analyses.integrals.logarithmic import logarithmic_integral
from library.analyses.integrals.logistic import logistic_integral
from library.analyses.integrals.sinusoidal import sinusoidal_integral
from library.statistics.rounding import rounded_value

def accumulated_area(equation_type, coefficients, start, end, precision = 4):
    """
    Evaluates the definite integral between two points for a specific function

    Parameters
    ----------
    equation_type : str
        Name of the type of function for which the definite integral must be evaluated (e.g., 'linear', 'quadratic')
    coefficients : list
        Coefficients of the original function to integrate
    start : int or float
        Value of the x-coordinate of the first point to use for evaluating the definite integral
    end : int or float
        Value of the x-coordinate of the second point to use for evaluating the definite integral
    precision : int, optional
        Maximum number of digits that can appear after the decimal place of the result

    Raises
    ------
    ValueError
        First argument must be either 'linear', 'quadratic', 'cubic', 'hyperbolic', 'exponential', 'logarithmic', 'logistic', or 'sinusoidal'
    TypeError
        Second argument must be a 1-dimensional list containing elements that are integers or floats
    TypeError
        Third and fourth arguments must be integers or floats
    ValueError
        Last argument must be a positive integer

    Returns
    -------
    area : float
        Definite integral of the original equation, evaluated between two points

    See Also
    --------
    :func:`~library.analyses.integrals.linear.linear_integral`, :func:`~library.analyses.integrals.quadratic.quadratic_integral`, :func:`~library.analyses.integrals.cubic.cubic_integral`, :func:`~library.analyses.integrals.hyperbolic.hyperbolic_integral`, :func:`~library.analyses.integrals.exponential.exponential_integral`, :func:`~library.analyses.integrals.logarithmic.logarithmic_integral`, :func:`~library.analyses.integrals.logistic.logistic_integral`, :func:`~library.analyses.integrals.sinusoidal.sinusoidal_integral`

    Notes
    -----
    - Definite integral: :math:`\\int_{a}^{b} f(x) \\,dx = F(b) - F(a)`
    - |definite_integral|
    - |fundamental_theorem|

    Examples
    --------
    Evaluate the definite integral of a linear function with coefficients 2 and 3 between the end points 10 and 20
        >>> area_linear = accumulated_area('linear', [2, 3], 10, 20)
        >>> print(area_linear)
        330.0
    Evaluate the definite integral of a cubic function with coefficients 8, 6, -10, and 7 between the end points 10 and 20
        >>> area_cubic = accumulated_area('cubic', [8, 6, -10, 7], 10, 20)
        >>> print(area_cubic)
        312570.0
    """
    select_equations(equation_type)
    vector_of_scalars(coefficients, 'second')
    compare_scalars(start, end, 'third', 'fourth')
    positive_integer(precision)
    integral = lambda x : x
    if equation_type == 'linear':
        integral = linear_integral(*coefficients)['evaluation']
    elif equation_type == 'quadratic':
        integral = quadratic_integral(*coefficients)['evaluation']
    elif equation_type == 'cubic':
        integral = cubic_integral(*coefficients)['evaluation']
    elif equation_type == 'hyperbolic':
        integral = hyperbolic_integral(*coefficients)['evaluation']
    elif equation_type == 'exponential':
        integral = exponential_integral(*coefficients)['evaluation']
    elif equation_type == 'logarithmic':
        integral = logarithmic_integral(*coefficients)['evaluation']
    elif equation_type == 'logistic':
        integral = logistic_integral(*coefficients)['evaluation']
    elif equation_type == 'sinusoidal':
        integral = sinusoidal_integral(*coefficients)['evaluation']
    area = integral(end) - integral(start)
    result = rounded_value(area, precision)
    return result