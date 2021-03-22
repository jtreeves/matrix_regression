import unittest

from library.analyses.equations.linear import linear as linear_equation
from library.analyses.equations.quadratic import quadratic as quadratic_equation
from library.analyses.equations.cubic import cubic as cubic_equation
from library.analyses.equations.hyperbolic import hyperbolic as hyperbolic_equation
from library.analyses.equations.exponential import exponential as exponential_equation
from library.analyses.equations.logarithmic import logarithmic as logarithmic_equation
from library.analyses.roots.linear import linear as linear_roots
from library.analyses.roots.quadratic import quadratic as quadratic_roots
from library.analyses.roots.cubic import cubic as cubic_roots
from library.analyses.roots.hyperbolic import hyperbolic as hyperbolic_roots
from library.analyses.roots.exponential import exponential as exponential_roots
from library.analyses.roots.logarithmic import logarithmic as logarithmic_roots
from library.analyses.derivatives.linear import linear as linear_derivatives
from library.analyses.derivatives.quadratic import quadratic as quadratic_derivatives
from library.analyses.derivatives.cubic import cubic as cubic_derivatives
from library.analyses.derivatives.hyperbolic import hyperbolic as hyperbolic_derivatives
from library.analyses.derivatives.exponential import exponential as exponential_derivatives
from library.analyses.derivatives.logarithmic import logarithmic as logarithmic_derivatives
from library.analyses.integrals.linear import linear as linear_integral
from library.analyses.integrals.quadratic import quadratic as quadratic_integral
from library.analyses.integrals.cubic import cubic as cubic_integral
from library.analyses.integrals.hyperbolic import hyperbolic as hyperbolic_integral
from library.analyses.integrals.exponential import exponential as exponential_integral
from library.analyses.integrals.logarithmic import logarithmic as logarithmic_integral
from library.analyses.critical_points import critical_points
from library.analyses.intervals import intervals
from library.analyses.intercepts import intercepts
from library.analyses.maxima import maxima
from library.analyses.minima import minima
from library.analyses.extrema import extrema
from library.analyses.inflections import inflections
from library.analyses.key_points import key_points
from library.analyses.accumulation import accumulation
from library.analyses.mean_values import average_values

coefficients = [2, 3, 5, 7]
precision = 4

linear_function = linear_equation(coefficients[0], coefficients[1])
quadratic_function = quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
cubic_function = cubic_equation(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_function = hyperbolic_equation(coefficients[0], coefficients[1])
exponential_function = exponential_equation(coefficients[0], coefficients[1])
logarithmic_function = logarithmic_equation(coefficients[0], coefficients[1])

class TestEquations(unittest.TestCase):
    def test_linear_function(self):
        self.assertEqual(linear_function(10), 23)
    
    def test_quadratic_function(self):
        self.assertEqual(quadratic_function(10), 235)
    
    def test_cubic_function(self):
        self.assertEqual(cubic_function(10), 2357)
    
    def test_hyperbolic_function(self):
        self.assertEqual(hyperbolic_function(10), 3.2)
    
    def test_exponential_function(self):
        self.assertEqual(exponential_function(10), 118098)
    
    def test_logarithmic_function(self):
        self.assertEqual(logarithmic_function(10), 7.605170185988092)

linear_derivatives_object = linear_derivatives(coefficients[0], coefficients[1])
quadratic_derivatives_object = quadratic_derivatives(coefficients[0], coefficients[1], coefficients[2])
cubic_derivatives_object = cubic_derivatives(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_derivatives_object = hyperbolic_derivatives(coefficients[0], coefficients[1])
exponential_derivatives_object = exponential_derivatives(coefficients[0], coefficients[1])
logarithmic_derivatives_object = logarithmic_derivatives(coefficients[0], coefficients[1])

class TestDerivatives(unittest.TestCase):
    def test_linear_derivatives_object_first_constants(self):
        self.assertEqual(linear_derivatives_object['first']['constants'], [2])
    
    def test_quadratic_derivatives_object_first_constants(self):
        self.assertEqual(quadratic_derivatives_object['first']['constants'], [4, 3])
    
    def test_cubic_derivatives_object_first_constants(self):
        self.assertEqual(cubic_derivatives_object['first']['constants'], [6, 6, 5])
    
    def test_hyperbolic_derivatives_object_first_constants(self):
        self.assertEqual(hyperbolic_derivatives_object['first']['constants'], [-2])
    
    def test_exponential_derivatives_object_first_constants(self):
        self.assertEqual(exponential_derivatives_object['first']['constants'], [2.1972245773362196, 3])
    
    def test_logarithmic_derivatives_object_first_constants(self):
        self.assertEqual(logarithmic_derivatives_object['first']['constants'], [2])
    
    def test_linear_derivatives_object_second_constants(self):
        self.assertEqual(linear_derivatives_object['second']['constants'], [0])
    
    def test_quadratic_derivatives_object_second_constants(self):
        self.assertEqual(quadratic_derivatives_object['second']['constants'], [4])
    
    def test_cubic_derivatives_object_second_constants(self):
        self.assertEqual(cubic_derivatives_object['second']['constants'], [12, 6])
    
    def test_hyperbolic_derivatives_object_second_constants(self):
        self.assertEqual(hyperbolic_derivatives_object['second']['constants'], [4])
    
    def test_exponential_derivatives_object_second_constants(self):
        self.assertEqual(exponential_derivatives_object['second']['constants'], [2.413897921625164, 3])
    
    def test_logarithmic_derivatives_object_second_constants(self):
        self.assertEqual(logarithmic_derivatives_object['second']['constants'], [-2])

linear_integral_object = linear_integral(coefficients[0], coefficients[1])
quadratic_integral_object = quadratic_integral(coefficients[0], coefficients[1], coefficients[2])
cubic_integral_object = cubic_integral(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
hyperbolic_integral_object = hyperbolic_integral(coefficients[0], coefficients[1])
exponential_integral_object = exponential_integral(coefficients[0], coefficients[1])
logarithmic_integral_object = logarithmic_integral(coefficients[0], coefficients[1])

class TestIntegrals(unittest.TestCase):
    def test_linear_integral_object(self):
        self.assertEqual(linear_integral_object['constants'], [1.0, 3])
    
    def test_quadratic_integral_object(self):
        self.assertEqual(quadratic_integral_object['constants'], [0.6666666666666666, 1.5, 5])
    
    def test_cubic_integral_object(self):
        self.assertEqual(cubic_integral_object['constants'], [0.5, 1.0, 2.5, 7])
    
    def test_hyperbolic_integral_object(self):
        self.assertEqual(hyperbolic_integral_object['constants'], [2, 3])
    
    def test_exponential_integral_object(self):
        self.assertEqual(exponential_integral_object['constants'], [1.8204784532536746, 3])
    
    def test_logarithmic_integral_object(self):
        self.assertEqual(logarithmic_integral_object['constants'], [2, 3])

first_linear_critical_points = critical_points('linear', 1, coefficients[:2], precision)
first_quadratic_critical_points = critical_points('quadratic', 1, coefficients[:3], precision)
first_cubic_critical_points = critical_points('cubic', 1, coefficients, precision)
first_hyperbolic_critical_points = critical_points('hyperbolic', 1, coefficients[:2], precision)
first_exponential_critical_points = critical_points('exponential', 1, coefficients[:2], precision)
first_logarithmic_critical_points = critical_points('logarithmic', 1, coefficients[:2], precision)

second_linear_critical_points = critical_points('linear', 2, coefficients[:2], precision)
second_quadratic_critical_points = critical_points('quadratic', 2, coefficients[:3], precision)
second_cubic_critical_points = critical_points('cubic', 2, coefficients, precision)
second_hyperbolic_critical_points = critical_points('hyperbolic', 2, coefficients[:2], precision)
second_exponential_critical_points = critical_points('exponential', 2, coefficients[:2], precision)
second_logarithmic_critical_points = critical_points('logarithmic', 2, coefficients[:2], precision)

class TestCriticalPoints(unittest.TestCase):
    def test_first_linear_critical_points(self):
        self.assertEqual(first_linear_critical_points, [None])
    
    def test_first_quadratic_critical_points(self):
        self.assertEqual(first_quadratic_critical_points, [-0.75])
    
    def test_first_cubic_critical_points(self):
        self.assertEqual(first_cubic_critical_points, [None])
    
    def test_first_hyperbolic_critical_points(self):
        self.assertEqual(first_hyperbolic_critical_points, [0])
    
    def test_first_exponential_critical_points(self):
        self.assertEqual(first_exponential_critical_points, [None])
    
    def test_first_logarithmic_critical_points(self):
        self.assertEqual(first_logarithmic_critical_points, [None])
    
    def test_second_linear_critical_points(self):
        self.assertEqual(second_linear_critical_points, [None])
    
    def test_second_quadratic_critical_points(self):
        self.assertEqual(second_quadratic_critical_points, [None])
    
    def test_second_cubic_critical_points(self):
        self.assertEqual(second_cubic_critical_points, [-0.5])
    
    def test_second_hyperbolic_critical_points(self):
        self.assertEqual(second_hyperbolic_critical_points, [0])
    
    def test_second_exponential_critical_points(self):
        self.assertEqual(second_exponential_critical_points, [None])
    
    def test_second_logarithmic_critical_points(self):
        self.assertEqual(second_logarithmic_critical_points, [None])

first_linear_intervals = intervals(linear_derivatives_object['first']['evaluation'], first_linear_critical_points)
first_quadratic_intervals = intervals(quadratic_derivatives_object['first']['evaluation'], first_quadratic_critical_points)
first_cubic_intervals = intervals(cubic_derivatives_object['first']['evaluation'], first_cubic_critical_points)
first_hyperbolic_intervals = intervals(hyperbolic_derivatives_object['first']['evaluation'], first_hyperbolic_critical_points)
first_exponential_intervals = intervals(exponential_derivatives_object['first']['evaluation'], first_exponential_critical_points)
first_logarithmic_intervals = intervals(logarithmic_derivatives_object['first']['evaluation'], first_logarithmic_critical_points)

second_linear_intervals = intervals(linear_derivatives_object['second']['evaluation'], second_linear_critical_points)
second_quadratic_intervals = intervals(quadratic_derivatives_object['second']['evaluation'], second_quadratic_critical_points)
second_cubic_intervals = intervals(cubic_derivatives_object['second']['evaluation'], second_cubic_critical_points)
second_hyperbolic_intervals = intervals(hyperbolic_derivatives_object['second']['evaluation'], second_hyperbolic_critical_points)
second_exponential_intervals = intervals(exponential_derivatives_object['second']['evaluation'], second_exponential_critical_points)
second_logarithmic_intervals = intervals(logarithmic_derivatives_object['second']['evaluation'], second_logarithmic_critical_points)

class TestIntervals(unittest.TestCase):
    def test_first_linear_intervals(self):
        self.assertEqual(first_linear_intervals, ['positive'])
    
    def test_first_quadratic_intervals(self):
        self.assertEqual(first_quadratic_intervals, ['negative', -0.75, 'positive'])
    
    def test_first_cubic_intervals(self):
        self.assertEqual(first_cubic_intervals, ['positive'])
    
    def test_first_hyperbolic_intervals(self):
        self.assertEqual(first_hyperbolic_intervals, ['negative', 0, 'negative'])
    
    def test_first_exponential_intervals(self):
        self.assertEqual(first_exponential_intervals, ['positive'])
    
    def test_first_logarithmic_intervals(self):
        self.assertEqual(first_logarithmic_intervals, ['positive'])
    
    def test_second_linear_intervals(self):
        self.assertEqual(second_linear_intervals, ['constant'])
    
    def test_second_quadratic_intervals(self):
        self.assertEqual(second_quadratic_intervals, ['positive'])
    
    def test_second_cubic_intervals(self):
        self.assertEqual(second_cubic_intervals, ['negative', -0.5, 'positive'])
    
    def test_second_hyperbolic_intervals(self):
        self.assertEqual(second_hyperbolic_intervals, ['negative', 0, 'positive'])
    
    def test_second_exponential_intervals(self):
        self.assertEqual(second_exponential_intervals, ['positive'])
    
    def test_second_logarithmic_intervals(self):
        self.assertEqual(second_logarithmic_intervals, ['negative'])

class TestRoots(unittest.TestCase):
    def test_linear_zeroes(self):
        linear_zeroes = linear_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(linear_zeroes, [-1.5])
    
    def test_quadratic_zeroes(self):
        quadratic_zeroes = quadratic_roots(coefficients[0], coefficients[1], coefficients[2], precision)
        self.assertEqual(quadratic_zeroes, [None])
    
    def test_cubic_zeroes(self):
        cubic_zeroes = cubic_roots(coefficients[0], coefficients[1], coefficients[2], coefficients[3], precision)
        self.assertEqual(cubic_zeroes, [-1.4455])
    
    def test_hyperbolic_zeroes(self):
        hyperbolic_zeroes = hyperbolic_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(hyperbolic_zeroes, [-0.6667])
    
    def test_exponential_zeroes(self):
        exponential_zeroes = exponential_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(exponential_zeroes, [None])
    
    def test_logarithmic_zeroes(self):
        logarithmic_zeroes = logarithmic_roots(coefficients[0], coefficients[1], precision)
        self.assertEqual(logarithmic_zeroes, [0.2231])

class TestIntercepts(unittest.TestCase):
    def test_linear_intercepts(self):
        linear_intercepts = intercepts('linear', coefficients[:2], precision)
        self.assertEqual(linear_intercepts, [-1.5])
    
    def test_quadratic_intercepts(self):
        quadratic_intercepts = intercepts('quadratic', coefficients[:3], precision)
        self.assertEqual(quadratic_intercepts, [None])
    
    def test_cubic_intercepts(self):
        cubic_intercepts = intercepts('cubic', coefficients, precision)
        self.assertEqual(cubic_intercepts, [-1.4455])
    
    def test_hyperbolic_intercepts(self):
        hyperbolic_intercepts = intercepts('hyperbolic', coefficients[:2], precision)
        self.assertEqual(hyperbolic_intercepts, [-0.6667])
    
    def test_exponential_intercepts(self):
        exponential_intercepts = intercepts('exponential', coefficients[:2], precision)
        self.assertEqual(exponential_intercepts, [None])
    
    def test_logarithmic_intercepts(self):
        logarithmic_intercepts = intercepts('logarithmic', coefficients[:2], precision)
        self.assertEqual(logarithmic_intercepts, [0.2231])

class TestMaxima(unittest.TestCase):
    def test_linear_maxima(self):
        linear_maxima = maxima(first_linear_intervals)
        self.assertEqual(linear_maxima, [None])
    
    def test_quadratic_maxima(self):
        quadratic_maxima = maxima(first_quadratic_intervals)
        self.assertEqual(quadratic_maxima, [None])
    
    def test_cubic_maxima(self):
        cubic_maxima = maxima(first_cubic_intervals)
        self.assertEqual(cubic_maxima, [None])
    
    def test_hyperbolic_maxima(self):
        hyperbolic_maxima = maxima(first_hyperbolic_intervals)
        self.assertEqual(hyperbolic_maxima, [None])
    
    def test_exponential_maxima(self):
        exponential_maxima = maxima(first_exponential_intervals)
        self.assertEqual(exponential_maxima, [None])
    
    def test_logarithmic_maxima(self):
        logarithmic_maxima = maxima(first_logarithmic_intervals)
        self.assertEqual(logarithmic_maxima, [None])

class TestMinima(unittest.TestCase):
    def test_linear_minima(self):
        linear_minima = minima(first_linear_intervals)
        self.assertEqual(linear_minima, [None])
    
    def test_quadratic_minima(self):
        quadratic_minima = minima(first_quadratic_intervals)
        self.assertEqual(quadratic_minima, [-0.75])
    
    def test_cubic_minima(self):
        cubic_minima = minima(first_cubic_intervals)
        self.assertEqual(cubic_minima, [None])
    
    def test_hyperbolic_minima(self):
        hyperbolic_minima = minima(first_hyperbolic_intervals)
        self.assertEqual(hyperbolic_minima, [None])
    
    def test_exponential_minima(self):
        exponential_minima = minima(first_exponential_intervals)
        self.assertEqual(exponential_minima, [None])
    
    def test_logarithmic_minima(self):
        logarithmic_minima = minima(first_logarithmic_intervals)
        self.assertEqual(logarithmic_minima, [None])

class TestExtrema(unittest.TestCase):
    def test_linear_extrema(self):
        linear_extrema = extrema('linear', coefficients[:2], linear_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(linear_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_quadratic_extrema(self):
        quadratic_extrema = extrema('quadratic', coefficients[:3], quadratic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(quadratic_extrema, {'maxima': [None], 'minima': [-0.75]})
    
    def test_cubic_extrema(self):
        cubic_extrema = extrema('cubic', coefficients, cubic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(cubic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_hyperbolic_extrema(self):
        hyperbolic_extrema = extrema('hyperbolic', coefficients[:2], hyperbolic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(hyperbolic_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_exponential_extrema(self):
        exponential_extrema = extrema('exponential', coefficients[:2], exponential_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(exponential_extrema, {'maxima': [None], 'minima': [None]})
    
    def test_logarithmic_extrema(self):
        logarithmic_extrema = extrema('logarithmic', coefficients[:2], logarithmic_derivatives_object['first']['evaluation'], precision)
        self.assertEqual(logarithmic_extrema, {'maxima': [None], 'minima': [None]})

class TestInflections(unittest.TestCase):
    def test_linear_inflections(self):
        linear_inflections = inflections('linear', coefficients[:2], linear_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(linear_inflections, [None])
    
    def test_quadratic_inflections(self):
        quadratic_inflections = inflections('quadratic', coefficients[:3], quadratic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(quadratic_inflections, [None])
    
    def test_cubic_inflections(self):
        cubic_inflections = inflections('cubic', coefficients, cubic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(cubic_inflections, [-0.5])
    
    def test_hyperbolic_inflections(self):
        hyperbolic_inflections = inflections('hyperbolic', coefficients[:2], hyperbolic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(hyperbolic_inflections, [None])
    
    def test_exponential_inflections(self):
        exponential_inflections = inflections('exponential', coefficients[:2], exponential_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(exponential_inflections, [None])
    
    def test_logarithmic_inflections(self):
        logarithmic_inflections = inflections('logarithmic', coefficients[:2], logarithmic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(logarithmic_inflections, [None])

class TestKeyPoints(unittest.TestCase):
    def test_linear_key_points(self):
        linear_key_points = key_points('linear', coefficients[:2], linear_function, linear_derivatives_object['first']['evaluation'], linear_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(linear_key_points, {'roots': [[-1.5, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_quadratic_key_points(self):
        quadratic_key_points = key_points('quadratic', coefficients[:3], quadratic_function, quadratic_derivatives_object['first']['evaluation'], quadratic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(quadratic_key_points, {'roots': [None], 'maxima': [None], 'minima': [[-0.75, 3.875]], 'inflections': [None]})
    
    def test_cubic_key_points(self):
        cubic_key_points = key_points('cubic', coefficients, cubic_function, cubic_derivatives_object['first']['evaluation'], cubic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(cubic_key_points, {'roots': [[-1.4455, 0]], 'maxima': [None], 'minima': [None], 'inflections': [[-0.5, 5.0]]})
    
    def test_hyperbolic_key_points(self):
        hyperbolic_key_points = key_points('hyperbolic', coefficients[:2], hyperbolic_function, hyperbolic_derivatives_object['first']['evaluation'], hyperbolic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(hyperbolic_key_points, {'roots': [[-0.6667, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_exponential_key_points(self):
        exponential_key_points = key_points('exponential', coefficients[:2], exponential_function, exponential_derivatives_object['first']['evaluation'], exponential_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(exponential_key_points, {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]})
    
    def test_logarithmic_key_points(self):
        logarithmic_key_points = key_points('logarithmic', coefficients[:2], logarithmic_function, logarithmic_derivatives_object['first']['evaluation'], logarithmic_derivatives_object['second']['evaluation'], precision)
        self.assertEqual(logarithmic_key_points, {'roots': [[0.2231, 0]], 'maxima': [None], 'minima': [None], 'inflections': [None]})

class TestAccumulation(unittest.TestCase):
    def test_linear_accumulation(self):
        linear_accumulation = accumulation(linear_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(linear_accumulation, 330.0)
    
    def test_quadratic_accumulation(self):
        quadratic_accumulation = accumulation(quadratic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(quadratic_accumulation, 5166.6667)
    
    def test_cubic_accumulation(self):
        cubic_accumulation = accumulation(cubic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(cubic_accumulation, 82820.0)
    
    def test_hyperbolic_accumulation(self):
        hyperbolic_accumulation = accumulation(hyperbolic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(hyperbolic_accumulation, 31.3863)
    
    def test_exponential_accumulation(self):
        exponential_accumulation = accumulation(exponential_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(exponential_accumulation, 6347508375.7293)
    
    def test_logarithmic_accumulation(self):
        logarithmic_accumulation = accumulation(logarithmic_integral_object['evaluation'], 10, 20, precision)
        self.assertEqual(logarithmic_accumulation, 83.7776)

class TestAverages(unittest.TestCase):
    def test_linear_averages(self):
        linear_averages = average_values('linear', linear_function, linear_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(linear_averages, {'average_value_derivative': 2.0, 'mean_values_derivative': ['All'], 'average_value_integral': 33.0, 'mean_values_integral': [15.0]})
    
    def test_quadratic_averages(self):
        quadratic_averages = average_values('quadratic', quadratic_function, quadratic_integral_object['evaluation'], 10, 20, coefficients[:3], precision)
        self.assertEqual(quadratic_averages, {'average_value_derivative': 63.0, 'mean_values_derivative': [15.0], 'average_value_integral': 516.6667, 'mean_values_integral': [15.2624]})
    
    def test_cubic_averages(self):
        cubic_averages = average_values('cubic', cubic_function, cubic_integral_object['evaluation'], 10, 20, coefficients, precision)
        self.assertEqual(cubic_averages, {'average_value_derivative': 1495.0, 'mean_values_derivative': [15.2665], 'average_value_integral': 8282.0, 'mean_values_integral': [15.5188]})
    
    def test_hyperbolic_averages(self):
        hyperbolic_averages = average_values('hyperbolic', hyperbolic_function, hyperbolic_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(hyperbolic_averages, {'average_value_derivative': -0.01, 'mean_values_derivative': [14.1421], 'average_value_integral': 3.1386, 'mean_values_integral': [14.43]})
    
    def test_exponential_averages(self):
        exponential_averages = average_values('exponential', exponential_function, exponential_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(exponential_averages, {'average_value_derivative': 697345070.4, 'mean_values_derivative': [17.8185], 'average_value_integral': 634750837.5729, 'mean_values_integral': [17.8185]})
    
    def test_logarithmic_averages(self):
        logarithmic_averages = average_values('logarithmic', logarithmic_function, logarithmic_integral_object['evaluation'], 10, 20, coefficients[:2], precision)
        self.assertEqual(logarithmic_averages, {'average_value_derivative': 0.1386, 'mean_values_derivative': [14.43], 'average_value_integral': 8.3778, 'mean_values_integral': [14.7155]})

if __name__ == '__main__':
    unittest.main()

# ---------- Ran 102 tests in 0.010s ---------- OK ---------- #