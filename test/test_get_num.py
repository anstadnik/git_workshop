"""This module contains tests for get_num"""
from unittest import TestCase
from unittest.mock import patch

from lib.get_num import get_num


@patch("builtins.input", lambda *args: "3")
class TestGetFiveNums(TestCase):
    """
    Test class for get_num

    """
    def test_get_num(self):
        """
        Test for get_num

        """
        num = get_num()
        self.assertEqual(num, 3)
