import unittest
from unittest.mock import patch, MagicMock

from concurrency.get_websites import load_url as load_url

class TestGetWebsites(unittest.TestCase):

    @patch('concurrency.get_websites.requests')
    def test_load_url_returns_data(self, m):
        """ Check that we're getting the data from a request object """
        m.get = MagicMock(return_value={'text': 'foo'})
        data = data = load_url('fazzbear')
        self.assertEqual(data, 'foo')

    @patch('concurrency.get_websites.requests')
    def test_load_called_with_correct_url(self, m):
        """ Check that we're making the request with the url we pass """
        m.get = MagicMock(return_value={'text': 'foo'})
        data = load_url('fakeurl')
        m.get.assert_called_with('fakeurl')

if __name__ == "__main__":
    unittest.main()