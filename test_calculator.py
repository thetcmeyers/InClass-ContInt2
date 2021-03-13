"""
    Unit testing with calc app
"""


import calculator


class TestCalculator:

    def test_add(self):
        assert 9 == calculator.add(4, 5)

    def test_sub(self):
        assert 9 == calculator.sub(10, 1)
