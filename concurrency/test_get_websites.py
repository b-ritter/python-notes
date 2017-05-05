import unittest
from unittest.mock import patch

from concurrency.get_websites import load_url as load_url

class TestGetWebsites(unittest.TestCase):

    @patch('concurrency.get_websites.requests')
    def test_load_url(self, m):
        """ Check that we're getting the data from a request object """
        m.get = lambda req: {'text': 'foo'}
        data = load_url('fakeurl')
        self.assertEqual(data, 'foo')

if __name__ == "__main__":
    unittest.main()