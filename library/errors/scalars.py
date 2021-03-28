def scalar_value(scalar, position):
    identifier = ''
    argument = 'argument'
    if position == 'only':
        identifier = argument
    else:
        identifier = position + ' ' + argument
    if not isinstance(scalar, (int, float)):
        raise TypeError(f'{identifier.capitalize()} must be an integer or a float')
    else:
        return f'{identifier.capitalize()} is an integer or a float'

def two_scalars(scalar_one, scalar_two):
    scalar_value(scalar_one, 'first')
    scalar_value(scalar_two, 'second')
    return 'Both first and second arguments are integers or floats'

def three_scalars(scalar_one, scalar_two, scalar_three):
    two_scalars(scalar_one, scalar_two)
    scalar_value(scalar_three, 'third')
    return 'First, second, and third arguments are all integers or floats'

def four_scalars(scalar_one, scalar_two, scalar_three, scalar_four):
    three_scalars(scalar_one, scalar_two, scalar_three)
    scalar_value(scalar_four, 'fourth')
    return 'First, second, third, and fourth arguments are all integers or floats'

def compare_scalars(scalar_one, scalar_two, position_one, position_two):
    scalar_value(scalar_one, position_one)
    scalar_value(scalar_two, position_two)
    if scalar_one >= scalar_two:
        raise ValueError(f'{position_one.capitalize()} argument must be less than {position_two} argument')
    else:
        return f'{position_one.capitalize()} argument is less than {position_two} argument'

def positive_integer(scalar):
    if not isinstance(scalar, int) or not scalar > 0:
        raise ValueError('Last argument must be a positive integer')
    else:
        return 'Last argument is a positive integer'

def whole_number(scalar, position):
    if not isinstance(scalar, int) or not scalar >= 0:
        raise ValueError(f'{position.capitalize()} argument must be a whole number')
    else:
        return f'{position.capitalize()} argument is a whole number'

def select_integers(scalar, choices):
    if scalar not in choices:
        raise ValueError(f'Second argument must be one of the following integers: {choices}')
    else:
        return f'Second argument is one of the following integers: {choices}'

def allow_none_scalar(scalar):
    if not isinstance(scalar, (int, float)) and scalar is not None:
        raise TypeError('First argument must be an integer, a float, or None')
    else:
        return 'First argument is an integer, a float, or None'