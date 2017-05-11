""" Unit tests to check a function that reads
an environment variable of a known name."""

import unittest
from unittest.mock import patch
import os

from systemops.get_env_var import host

class TestGetHost(unittest.TestCase):
    """ Tests reading a value from the system environment. """

    @patch.dict(os.environ, {"local": "1.2.3.4"})
    def test_get_env_var(self):
        """ Should return a value for an environment variable called 'local' """
        hostname = host()
        self.assertEqual(hostname, "1.2.3.4")

    @patch.dict(os.environ, {"loko": "foo.bar.baz"})
    def test_get_env_var_oserror(self):
        """ Should throw an OS Error when the value is not found """
        with self.assertRaises(OSError):
            host()

if __name__ == "__main__":
    unittest.main()
