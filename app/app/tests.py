"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)

    def test_subtract_nummbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(12, 10)

        self.assertEqual(res, 2)