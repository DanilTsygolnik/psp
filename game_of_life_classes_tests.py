import unittest
from game_of_life_classes import *

class TestCell(unittest.TestCase):
    '''dev step 2.1'''

    def setUp(self):
        height_coord = 1
        width_coord = 1
        self.test_cell = Cell(height_coord, width_coord)

    def test_get_cell_id(self):
        cell_id = "h1w1"
        self.assertEqual(self.test_cell.get_cell_id(), cell_id)

    def test_get_cell_height(self):
        height_coord = 1
        self.assertEqual(self.test_cell.get_cell_height(), height_coord)

    def test_get_cell_width(self):
        width_coord = 1
        self.assertEqual(self.test_cell.get_cell_width(), width_coord)

    def test_get_cell_status(self):
        self.assertFalse(self.test_cell.get_cell_status())

    def test_set_cell_status(self):
        self.test_cell.set_cell_status(True)
        self.assertTrue(self.test_cell.get_cell_status())

    def test_get_neighbors_ids(self):
        self.assertIs(self.test_cell.get_neighbors_ids(), None)

    def test_add_neighbors_ids(self):
        neighbors_ids = set(["h2w1", "h0w1"])
        self.test_cell.add_neighbors_ids(neighbors_ids)
        self.assertEqual(self.test_cell.get_neighbors_ids(), neighbors_ids)

    def test_get_neighbors(self):
        self.assertIs(self.test_cell.get_neighbors(), None)

    def test_add_neighbors(self):
        test_set = set()
        self.test_cell.add_neighbors(test_set)
        self.assertEqual(self.test_cell.get_neighbors(), test_set)


if __name__=="__main__":
    unittest.main()
