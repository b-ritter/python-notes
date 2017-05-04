import unittest

from years.years_as_string_list import years

class TestYears(unittest.TestCase):

    def test_years_returns_correct_values(self):
        self.assertListEqual(years(2000, 2003), ['2000', '2001', '2002', '2003'])

if __name__ == "__main__":
    unittest.main()
