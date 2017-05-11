""" Explore how python works with lambda expressions. """
import unittest
import string
import random

class TestGetWebsites(unittest.TestCase):

    def test_closure(self, m):
        """ See that python supports closures similar to JavaScript """
        def gibberish():
            """ Some random string """
            return ''.join([random.choice(string.ascii_letters) for i in range(20)])
        value1 = gibberish()
        value2 = gibberish()
        result = (lambda x: lambda y: x)(value1)(value2)
        self.assertEqual(result, value1)

if __name__ == "__main__":
    unittest.main()