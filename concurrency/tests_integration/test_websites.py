from concurrency.get_websites import get_number_of_links
import time

# Run get_number_of_links and compare it to a serial version
# stub out load_url with a sleep function so the time is always the same
# Show that the concurrent version takes less time than the serial


import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from concurrency.get_websites import get_number_of_links

class TestConcurrency(unittest.TestCase):

    def setUp(self):
        self.loadtime = 1

    @patch('concurrency.get_websites.BeautifulSoup')
    @patch('concurrency.get_websites.load_url')
    def test_concurrent_slower_than_serial(self, mock_load_url, bs_mock):
        """ Time the collection of data from websites """
        bs_data = MagicMock(return_value=['link1', 'link2'])
        bs_mock.return_value = bs_data
        mock_load_url.side_effect = lambda foo: time.sleep(self.loadtime)
        concurrent_start = time.time()
        list(get_number_of_links(['url1','url2']))
        concurrent_total = time.time() - concurrent_start
        print(concurrent_total)

if __name__ == "__main__":
    unittest.main()