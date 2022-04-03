import unittest
from play_round import *
from player_class import *

class TestStage2(unittest.TestCase):

    def test_choose_winner(self):
        self.assertEqual(choose_winner("1"), 1)
        self.assertEqual(choose_winner("2"), 2)
        self.assertEqual(choose_winner("0"), 0)
        self.assertEqual(choose_winner(""), "wrong_input")

if __name__=="__main__":
    unittest.main()
