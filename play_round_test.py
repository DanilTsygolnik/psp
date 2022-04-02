import unittest
from play_round import *
from player_class import *

class TestStage2(unittest.TestCase):

    def test_choose_winner(self):
        self.assertEqual(choose_winner("1"), 1)
        self.assertEqual(choose_winner("2"), 2)
        self.assertEqual(choose_winner("0"), 0)
        self.assertEqual(choose_winner(""), "wrong_input")

    def test_update_score(self):
        player1 = Player()
        player2 = Player()
        self.assertEqual(update_score(1, player1, player2), 1)
        self.assertEqual(player1.get_score(), 1)
        self.assertEqual(update_score(2, player1, player2), 2)
        self.assertEqual(player2.get_score(), 1)

if __name__=="__main__":
    unittest.main()
