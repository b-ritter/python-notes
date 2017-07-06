import unittest
from unittest.mock import patch, MagicMock, mock_open
from systemops.yaml_opener import get_stuff

class TestYaml(unittest.TestCase):
    mock_data = "foo: bar"

    @patch('systemops.yaml_opener.open', mock_open(read_data=mock_data))
    def test_yaml_open(self):
        result = get_stuff('fake.yml')
        self.assertEqual(result, self.mock_data)
        