import unittest
import json
from unittest.mock import patch, MagicMock, mock_open

from systemops.opener import get_stooges

class TestOpener(unittest.TestCase):
    """ Tests opening and retrieving data from json """

    @patch('systemops.opener.open', mock_open(read_data='{"beer":"duff"}'))
    def test_get_stooges(self):
        result = get_stooges('homer.json')
        expected_result = json.loads('{"beer":"duff"}')
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()