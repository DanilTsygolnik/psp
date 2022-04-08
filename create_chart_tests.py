import unittest
from create_chart import *
from game_of_life_classes import *

# stage 2.2
class TestGetNeighborsIds(unittest.TestCase):

    def setUp(self):
        self.is_not_alive = False

    def test_map1x1(self):
        chart_height = 1
        chart_width = 1
        height_coord = 1
        width_coord = 1
        test_cell = Cell(height_coord, width_coord, self.is_not_alive)
        correct_output = set()
        test_output = get_neighbors_ids(test_cell, chart_height, chart_width)
        self.assertEqual(test_output, correct_output)

    # map view (x - cell, * - cells on chart)
    #   1 2
    # 1 x *
    # 1 * *
    def test_map2x2(self):
        chart_height = 2
        chart_width = 2
        height_coord = 1
        width_coord = 1
        test_cell = Cell(height_coord, width_coord, self.is_not_alive)
        correct_output = set(["h1w2","h2w1","h2w2"])
        test_output = get_neighbors_ids(test_cell, chart_height, chart_width)
        self.assertEqual(test_output, correct_output)

    # map view (x - cell, * - cells on chart)
    #   1 2 3
    # 1 * * *
    # 1 * x *
    # 1 * * *
    def test_map3x3(self):
        chart_height = 3
        chart_width = 3
        height_coord = 2
        width_coord = 2
        test_cell = Cell(height_coord, width_coord, self.is_not_alive)
        correct_output = set(["h1w1","h1w2","h1w3",
                              "h2w1",       "h2w3",
                              "h3w1","h3w2","h3w3"])
        test_output = get_neighbors_ids(test_cell, chart_height, chart_width)
        self.assertEqual(test_output, correct_output)


if __name__=="__main__":
    unittest.main()
