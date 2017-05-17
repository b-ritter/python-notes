import unittest

from lists.tuples import list_diff

class TestTuples(unittest.TestCase):

    def test_list_diff(self):
        list_a = [1, 2, 'foo', {'bar': 'baz'}, ('xyz',)]
        list_b = ['foo', {'bar': 'baz'}]
        result = list_diff(list_a, list_b)
        self.assertEqual([1, 2, ('xyz',)], result)

if __name__ == "__main__":
    unittest.main()
