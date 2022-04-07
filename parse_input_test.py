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

    def test_search_alive_in_string(self):
        string_num = 3
        input_string = "......"
        test_output = search_alive_in_string(string_num, input_string)
        correct_output = []
        self.assertEqual(test_output, correct_output)

        string_num = 3
        input_string = "...*..*..*"
        test_output = search_alive_in_string(string_num, input_string)
        correct_output = ["h3w4", "h3w7", "h3w10"]
        self.assertEqual(test_output, correct_output)

    def test_get_alive_cells_ids(self):
        input_file = "task_input.txt"

        with self.assertRaises(TypeError):
            get_alive_cells_ids(0, input_file)

        test_output = get_alive_cells_ids({}, input_file)
        correct_output = {'alive_cells_ids':["h2w5", "h3w4", "h3w5"]}
        self.assertEqual(test_output, correct_output)

class TestParse(unittest.TestCase):

    def test_main(self):
        input_file = "task_input.txt"
        test_output = parse_input(input_file)
        correct_output = {'height': 4, 'width': 8, 'alive_cells_ids':["h2w5", "h3w4", "h3w5"]}
        self.assertEqual(test_output, correct_output)

if __name__=="__main__":
    unittest.main()
