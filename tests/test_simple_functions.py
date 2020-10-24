import pytest
import numpy as np
from simple_functions import mysin, factorial


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    def test_pi(self):
        '''Test computation of pi'''
        irange = np.linspace(0, 1, 5)
        for i in irange:
            my_sin = mysin(i * np.pi, 10)
            assert np.isclose(my_sin, np.sin(i * np.pi), atol=1e-6)
