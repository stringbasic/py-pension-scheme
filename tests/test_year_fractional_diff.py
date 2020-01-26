import unittest
from pension.helper_functions import year_fractional_diff
from datetime import date

class YearFractionalDiffTest(unittest.TestCase):
    def test_four_years(self):
        dstart = date(2016,1,1)
        dend = date(2020,1,1)
        self.assertEqual(year_fractional_diff(dstart, dend), 4.0)

    def test_four_years_negative(self):
        dstart = date(2016,1,1)
        dend = date(2020,1,1)
        self.assertEqual(year_fractional_diff(dend, dstart), -4.0)
