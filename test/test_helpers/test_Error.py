import unittest

from helpers.Error import Error


class TestError(unittest.TestCase):

    def test_errorMessage(self):
        error = Error("test")
        self.assertEqual("test", error.errorMessage())
