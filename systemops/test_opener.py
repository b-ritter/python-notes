import unittest
import json
import os
import sys
from unittest.mock import patch, MagicMock, mock_open

from systemops.opener import get_stooges
from settings import ROOT_DIR

class TestOpener(unittest.TestCase):
    """ Tests opening and retrieving data from json """

    @patch('systemops.opener.open', mock_open(read_data='{"beer":"duff"}'))
    def test_get_stooges(self):
        """ Checks whether the json getter returns the expected value """
        result = get_stooges('homer.json')
        expected_result = json.loads('{"beer":"duff"}')
        self.assertEqual(expected_result, result)

    def test_data_exists(self):
        """ Checks that data file exists"""
        self.assertTrue(get_stooges(os.path.join(ROOT_DIR, 'systemops/data/stooges.json')))

if __name__ == "__main__":
    unittest.main()