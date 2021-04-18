from math import log
from library.errors.scalars import two_scalars, positive_integer
from library.errors.adjustments import no_zeroes
from library.statistics.rounding import rounded_value

def logarithmic_integral(first_constant, second_constant, precision = 4):
    """
    Generates the integral of a logarithmic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the logarithmic term of the original logarithmic function; if zero, it will be converted to a small, non-zero decimal value (e.g., 0.0001)
    second_constant : int or float
        Coefficient of the constant term of the original logarithmic function; if zero, it will be converted to a small, non-zero decimal value (e.g., 0.0001)
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
    integral['constants'] : list of float
        Coefficients of the resultant integral
    integral['evaluation'] : func
        Function for evaluating the resultant integral at any float or integer argument; if zero inputted as argument, it will be converted to a small, non-zero decimal value (e.g., 0.0001)

    See Also
    --------
    :func:`~library.analyses.equations.logarithmic.logarithmic_equation`, :func:`~library.analyses.derivatives.logarithmic.logarithmic_derivatives`, :func:`~library.analyses.roots.logarithmic.logarithmic_roots`, :func:`~library.models.logarithmic.logarithmic_model`

    Notes
    -----
    - Standard form of a logarithmic function: :math:`f(x) = a\\cdot{\\ln{x}} + b`
    - Integral of a logarithmic function: :math:`F(x) = a\\cdot{x}\\cdot(\\ln{x} - 1) + b\\cdot{x}`
    - |indefinite_integral|
    - |integration_formulas|
    - |integration_by_parts|

    Examples
    --------
    Generate the integral of a logarithmic function with coefficients 2 and 3, then display its coefficients
        >>> integral_constants = logarithmic_integral(2, 3)
        >>> print(integral_constants['constants'])
        [2.0, 3.0]
    Generate the integral of a logarithmic function with coefficients -2 and 3, then evaluate its integral at 10
        >>> integral_evaluation = logarithmic_integral(-2, 3)
        >>> print(integral_evaluation['evaluation'](10))
        3.9483
    Generate the integral of a logarithmic function with all inputs set to 0, then display its coefficients
        >>> integral_zeroes = logarithmic_integral(0, 0)
        >>> print(integral_zeroes['constants'])
        [0.0001, 0.0001]
    """
    # Handle input errors
    two_scalars(first_constant, second_constant)
    positive_integer(precision)
    coefficients = no_zeroes([first_constant, second_constant], precision)

    # Create constants
    constants = [coefficients[0], coefficients[1]]

    # Create evaluation
    def logarithmic_evaluation(variable):
        # Circumvent logarithm of zero
        if variable == 0:
            variable = 10**(-precision)
        evaluation = constants[0] * variable * (log(abs(variable)) - 1) + constants[1] * variable
        rounded_evaluation = rounded_value(evaluation, precision)
        return rounded_evaluation
    
    # Package constants and evaluation in single dictionary
    results = {
        'constants': constants,
        'evaluation': logarithmic_evaluation
    }
    return results