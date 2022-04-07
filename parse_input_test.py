import unittest
from parse_input import *

class TestGetChartDimensions(unittest.TestCase):
    ''' dev step 1.1'''

    def test_empty_input(self):
        empty_file_output = get_chart_sizes("empty_input.txt")
        correct_output = 0
        self.assertEqual(empty_file_output, correct_output)

    def test_standard_input(self):
        test_output = get_chart_sizes("task_input.txt")
        correct_output = {'height': 4, 'width': 8}
        self.assertEqual(test_output, correct_output)

class TestSearchAliveInString(unittest.TestCase):

    def test_no_alive_cells_in_string(self):
        string_num = 3
        input_string = "......"
        test_output = search_alive_in_string(string_num, input_string)
        correct_output = []
        self.assertEqual(test_output, correct_output)

    def test_alive_cells_in_string(self):
        string_num = 3
        input_string = "...*..*..*"
        test_output = search_alive_in_string(string_num, input_string)
        correct_output = ["h3w4", "h3w7", "h3w10"]
        self.assertEqual(test_output, correct_output)

class TestGetAliveCellsIds(unittest.TestCase):

    def setUp(self):
        self.input_file = "task_input.txt"

    def test_input_type_checking(self):
        with self.assertRaises(TypeError):
            get_alive_cells_ids(0, self.input_file)

    def test_get_alive_cells_ids(self):
        test_output = get_alive_cells_ids({}, self.input_file)
        correct_output = {'alive_cells_ids':["h2w5", "h3w4", "h3w5"]}
        self.assertEqual(test_output, correct_output)

class TestParseInput(unittest.TestCase):

    def test_main(self):
        input_file = "task_input.txt"
        test_output = parse_input(input_file)
        correct_output = {'height': 4, 'width': 8, 'alive_cells_ids':["h2w5", "h3w4", "h3w5"]}
        self.assertEqual(test_output, correct_output)

if __name__=="__main__":
    unittest.main()
