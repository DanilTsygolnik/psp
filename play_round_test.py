import unittest
from play_round import *
from player_class import *

class TestStage3(unittest.TestCase):

    def test_choose_winner(self):
        self.assertEqual(choose_winner("1"), 1)
        self.assertEqual(choose_winner("2"), 2)
        self.assertEqual(choose_winner("0"), 0)
        self.assertEqual(choose_winner(""), "wrong_input")

    def test_show_scores(self):
        player_one = Player("20")
        player_two = Player("30")
        round_num = 2
        testing_on = True
        correct_output = "".join(["==== Round 2 score ====\n",
                                  "Player 1 -- 20\n",
                                   "Player 2 -- 30" ])
        test_output = show_scores(round_num, player_one, player_two, testing_on)
        self.assertEqual(test_output, correct_output)

if __name__=="__main__":
    unittest.main()
