from unittest import TestCase
from unittest.mock import patch
from lib.get_num import get_num

# def mock_input(dummy_prompt):
#     return 3

@patch('builtins.input', lambda *args: '3')
class TestGetFiveNums(TestCase):
    # def setUp(self):
    #     self.saved_input = __builtins__.input
    #     __builtins__.input = mock_input

    # def tearDown(self):
    #     __builtins__.input = self.saved_input

    def testGetFiveNums(self):
        num = get_num()
        self.assertEqual(num, 3)
