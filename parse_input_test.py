import unittest
from parse_input import *

class TestParseInput(unittest.TestCase):

    def test_get_chart_sizes(self):
        test_output = get_chart_sizes("task_input.txt")
        correct_output = {'height': 4, 'width': 8}
        self.assertEqual(test_output, correct_output)

        empty_file_output = get_chart_sizes("empty_input.txt")
        correct_output = 0
        self.assertEqual(empty_file_output, correct_output)

if __name__=="__main__":
    unittest.main()
