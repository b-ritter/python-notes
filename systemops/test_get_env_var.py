import unittest
import json
import os
from unittest.mock import patch, MagicMock, mock_open

from systemops.get_env_var import host

class TestGetHost(unittest.TestCase):
    """ Tests reading a value from the system environment. """

    @patch.dict(os.environ, {"local": "1.2.3.4"})
    def test_get_env_var(self):
        hostname = host()
        self.assertEqual(hostname, "1.2.3.4")

    @patch.dict(os.environ, {"loko": "foo.bar.baz"})
    def test_get_env_var_oserror(self):
        with self.assertRaises(OSError):
            host()

if __name__ == "__main__":
    unittest.main()