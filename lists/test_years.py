import unittest

from lists.years_as_string_list import years

class TestYears(unittest.TestCase):

    def test_years_returns_correct_values(self):
        self.assertListEqual(years(2000, 2003), ['2000', '2001', '2002', '2003'])

    def test_years_too_far_in_past(self):
        with self.assertRaises(ValueError):
            years(1900, 2001)

    def test_years_too_far_in_future(self):
        with self.assertRaises(ValueError):
            years(2000, 2025)

    def test_both_years_bad(self):
        with self.assertRaises(ValueError):
            years(1784, 2025)

if __name__ == "__main__":
    unittest.main()
