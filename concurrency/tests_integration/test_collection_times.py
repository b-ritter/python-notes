from concurrency.get_websites import get_number_of_links
import time

# Run get_number_of_links and compare it to a serial version
# stub out load_url with a sleep function so the time is always the same
# Show that the concurrent version takes less time than the serial


import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from concurrency.get_websites import get_number_of_links, get_number_of_links_serial

class TestConcurrency(unittest.TestCase):

    def setUp(self):
        self.loadtime = 1
        self.fake_urls = ['url1','url2', 'url3']

    @patch('concurrency.get_websites.BeautifulSoup')
    @patch('concurrency.get_websites.load_url')
    def test_concurrent_slower_than_serial(self, mock_load_url, bs_mock):
        """ Time the collection of data from websites """
        bs_data = MagicMock(return_value=["<a href='foo'>Baz</a>"])
        bs_mock.return_value = bs_data
        mock_load_url.side_effect = lambda foo: time.sleep(self.loadtime)
        concurrent_start = time.time()
        list(get_number_of_links(self.fake_urls))
        concurrent_total = time.time() - concurrent_start

        serial_start = time.time()
        get_number_of_links_serial(self.fake_urls)
        serial_total = time.time() - serial_start
        print("Concurrent collection: {}".format(concurrent_total))
        print("Serial collection: {}".format(serial_total))
        self.assertLess(concurrent_total, serial_total)

if __name__ == "__main__":
    unittest.main()