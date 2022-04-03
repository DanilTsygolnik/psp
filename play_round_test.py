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

class TestDefineScenario(unittest.TestCase):

    def test_1(self):
        user_choice = 1
        player_one = Player("40+")
        player_two = Player("40")
        game_in_deuce = True
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Player 1 wins"
        self.assertEqual(test_output, correct_output)

    def test_2(self):
        user_choice = 2
        player_one = Player("30")
        player_two = Player("40")
        game_in_deuce = False
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Player 2 wins"
        self.assertEqual(test_output, correct_output)

    def test_3(self):
        user_choice = 1
        player_one = Player("40")
        player_two = Player("40")
        game_in_deuce = True
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Player 1 has advantage"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "40+")

    def test_4(self):
        user_choice = 1
        player_one = Player("40")
        player_two = Player("40+")
        game_in_deuce = True
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_two.get_score(), "40")

    def test_5(self):
        user_choice = 1
        player_one = Player("30")
        player_two = Player("40")
        game_in_deuce = False
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "40")
        self.assertTrue(game_in_deuce)

    def test_6(self):
        user_choice = 1
        player_one = Player("30")
        player_two = Player("30")
        game_in_deuce = False
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "40")

    def test_7(self):
        user_choice = 1
        player_one = Player("15")
        player_two = Player("30")
        game_in_deuce = False
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "30")

    def test_8(self):
        user_choice = 1
        player_one = Player("love")
        player_two = Player("30")
        game_in_deuce = False
        test_output = define_scenario(user_choice, player_one, player_two, game_in_deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "15")

if __name__=="__main__":
    unittest.main()
