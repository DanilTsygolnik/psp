import unittest
from parse_input import *

class TestGetChartSizes(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_chart_sizes("task_input.txt"), [4,8])

if __name__=="__main__":
    unittest.main()
