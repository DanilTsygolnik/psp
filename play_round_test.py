import unittest
from play_round import *
from player_class import *
from deuce_class import *

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

    def setUp(self):
        self.deuce = Deuce()

    def test_1(self):
        user_choice = 1
        player_one = Player("40+")
        player_two = Player("40")
        self.deuce.set_value(True)
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Player 1 wins"
        self.assertEqual(test_output, correct_output)

    def test_2(self):
        user_choice = 2
        player_one = Player("30")
        player_two = Player("40")
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Player 2 wins"
        self.assertEqual(test_output, correct_output)

    def test_3(self):
        user_choice = 1
        player_one = Player("40")
        player_two = Player("40")
        self.deuce.set_value(True)
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Player 1 has advantage"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "40+")

    def test_4(self):
        user_choice = 1
        player_one = Player("40")
        player_two = Player("40+")
        self.deuce.set_value(True)
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_two.get_score(), "40")

    def test_5(self):
        user_choice = 1
        player_one = Player("30")
        player_two = Player("40")
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "40")
        self.assertTrue(self.deuce)

    def test_6(self):
        user_choice = 1
        player_one = Player("30")
        player_two = Player("30")
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "40")

    def test_7(self):
        user_choice = 1
        player_one = Player("15")
        player_two = Player("30")
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "30")

    def test_8(self):
        user_choice = 1
        player_one = Player("love")
        player_two = Player("30")
        test_output = define_scenario(user_choice, player_one, player_two, self.deuce)
        correct_output = "Going to next round"
        self.assertEqual(test_output, correct_output)
        self.assertEqual(player_one.get_score(), "15")

class TestFinishRound(unittest.TestCase):

    def test_1(self):
        scenario_id = "Player 1 wins"
        test_result = finish_round(scenario_id, True)
        correct_output = "game over"
        self.assertEqual(test_result, correct_output)

    def test_2(self):
        scenario_id = "Player 2 wins"
        test_result = finish_round(scenario_id, True)
        correct_output = "game over"
        self.assertEqual(test_result, correct_output)

    def test_3(self):
        scenario_id = "Player 1 has advantage"
        test_result = finish_round(scenario_id, True)
        correct_output = "next round"
        self.assertEqual(test_result, correct_output)

    def test_4(self):
        scenario_id = "Player 2 has advantage"
        test_result = finish_round(scenario_id, True)
        correct_output = "next round"
        self.assertEqual(test_result, correct_output)

    def test_5(self):
        scenario_id = "Going to next round"
        test_result = finish_round(scenario_id, True)
        correct_output = "next round"
        self.assertEqual(test_result, correct_output)


if __name__=="__main__":
    unittest.main()
