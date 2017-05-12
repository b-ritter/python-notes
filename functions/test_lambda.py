""" Explore how python works with lambda expressions. """
import unittest
import string
import random

class TestGetWebsites(unittest.TestCase):

    def test_closure(self):
        """ See that python supports closures similar to JavaScript """
        def gibberish():
            """ Some random string """
            return ''.join([random.choice(string.ascii_letters) for i in range(20)])
        value1 = gibberish()
        result = (lambda x: lambda: x)(value1)()
        self.assertEqual(result, value1)

    def test_closure_ids(self):
        """ Show how a variable passed to a function remains in scope
        even after it returns """
        def make_lambdas(num):
            """ Build a lambda generator """
            for i in range(num):
                func = lambda x: lambda: x
                yield func(i)
        functions = list(make_lambdas(random.randint(1, 10)))
        random_index = random.randint(0, len(functions)-1)
        random_function = functions[random_index]()
        print("{0} equals {1}".format(random_index, random_function))
        self.assertEqual(random_function, random_index)

if __name__ == "__main__":
    unittest.main()