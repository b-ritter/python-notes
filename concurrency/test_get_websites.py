import unittest
from requests import Request
from unittest.mock import patch, MagicMock

from concurrency.get_websites import load_url as load_url

class MockResponse():
    def __init__(self):
        self.text = "foo"
        self.status_code = 200

class TestGetWebsites(unittest.TestCase):

    @patch('concurrency.get_websites.requests')
    def test_load_url_returns_data(self, m):
        """ Check that we're getting the data from a request object """
        m.get = MagicMock(return_value=MockResponse())
        data = load_url('fazzbear')
        self.assertEqual(data, 'foo')

    @patch('concurrency.get_websites.requests')
    def test_load_called_with_correct_url(self, m):
        """ Check that we're making the request with the url we pass """
        m.get = MagicMock(return_value=MockResponse())
        load_url('fakeurl')
        m.get.assert_called_with('fakeurl')

if __name__ == "__main__":
    unittest.main()