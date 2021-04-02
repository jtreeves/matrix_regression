from library.errors.scalars import four_scalars

def cubic_derivatives(first_constant, second_constant, third_constant, fourth_constant):
    """
    Calculates the first and second derivatives of a cubic function

    Parameters
    ----------
    first_constant : int or float
        Coefficient of the cubic term of the original cubic function
    second_constant : int or float
        Coefficient of the quadratic term of the original cubic function
    third_constant : int or float
        Coefficient of the linear term of the original cubic function
    fourth_constant : int or float
        Coefficient of the constant term of the original cubic function

    Raises
    ------
    TypeError
        Arguments must be integers or floats

    Returns
    -------
    derivatives['first']['constants'] : list
        Coefficients of the resultant first derivative
    derivatives['first']['evaluation'] : function
        Function for evaluating the resultant first derivative at any float or integer argument
    derivatives['second']['constants'] : list
        Coefficients of the resultant second derivative
    derivatives['second']['evaluation'] : function
        Function for evaluating the resultant second derivative at any float or integer argument

    Examples
    --------
    Generate the derivatives of a cubic function with coefficients 2, 3, 5, and 7
        >>> derivatives = cubic_derivatives(2, 3, 5, 7)
    Print the coefficients of the first derivative
        >>> print(derivatives['first']['constants'])
        [6, 6, 5]
    Print the evaluation of the second derivative at an input of 10
        >>> print(derivatives['second']['evaluation'](10))
        126
    """
    four_scalars(first_constant, second_constant, third_constant, fourth_constant)
    first_constants = [3 * first_constant, 2 * second_constant, third_constant]
    def first_derivative(variable):
        evaluation = first_constants[0] * variable**2 + first_constants[1] * variable + first_constants[2]
        return evaluation
    first_object = {
        'constants': first_constants,
        'evaluation': first_derivative
    }
    second_constants = [2 * first_constants[0], first_constants[1]]
    def second_derivative(variable):
        evaluation = second_constants[0] * variable + second_constants[1]
        return evaluation
    second_object = {
        'constants': second_constants,
        'evaluation': second_derivative
    }
    results = {
        'first': first_object,
        'second': second_object
    }
    return results