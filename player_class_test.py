import unittest
from player_class import *

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_one = Player()
        self.player_two = Player("40")

    def test_constructor(self):
        self.assertEqual(self.player_one.get_score(), "love")
        self.assertEqual(self.player_two.get_score(), "40")

    def test_set_score(self):
        self.player_one.set_score("40")
        self.assertEqual(self.player_one.get_score(), "40")

if __name__=="__main__":
    unittest.main()
