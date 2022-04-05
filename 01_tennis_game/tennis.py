from enter_menu import *
from player_class import *
from deuce_class import *

def choose_winner(test_input=None):
    print("Please, choose the winner of this round.\n",
          "Enter 1 for player1; 2 for player2; 0 to finish the game.")
    testing = (test_input is not None)
    if not testing:
        user_choice = str(input())
    else:
        user_choice = test_input

    if user_choice == "1":
        return 1
    if user_choice == "2":
        return 2
    if user_choice == "0":
        return 0
    if not testing:
        print("Wrong input. Please try again.")
        return choose_winner(None)
    return "wrong_input"

def show_scores(round_num, player_one, player_two):
    print("".join( [ "==== ", "Round ", str(round_num), " score ===="]))
    print(" ".join(["Player 1 -- ", player_one.get_score()]))
    print(" ".join(["Player 2 -- ", player_two.get_score()]))

def define_scenario(user_choice, player_one, player_two, deuce_status):
    player_one_wins = (user_choice == 1)
    if player_one_wins:
        leader = player_one
        loser = player_two
        scenario_id_template = "Player 1 "
    else:
        leader = player_two
        loser = player_one
        scenario_id_template = "Player 2 "
    leader_score = leader.get_score()
    loser_score = loser.get_score()
    if leader_score == "40+":
        scenario_id = "".join([scenario_id_template, "wins"])
        return scenario_id
    game_in_deuce = deuce_status.check()
    if leader_score == "40":
        if not game_in_deuce:
            scenario_id = "".join([scenario_id_template, "wins"])
            return scenario_id
        if loser_score == "40":
            leader.set_score("40+")
            scenario_id = "".join([scenario_id_template, "has advantage"])
            return scenario_id
        loser.set_score("40")
    if leader_score == "30":
        leader.set_score("40")
        if loser_score == "40":
            deuce_status.set_value(True)
    if leader_score == "15":
        leader.set_score("30")
    if leader_score == "love":
        leader.set_score("15")
    scenario_id = "Going to next round"
    return scenario_id


def play_round(round_num, player_one, player_two, deuce_status):

    def finish_round(scenario_id):
        print(scenario_id)
        game_over = (scenario_id in ["Player 1 wins", "Player 2 wins"])
        if game_over:
            #return enter_menu("menu_template.txt")
            return tennis()
        return play_round(round_num+1, player_one, player_two, deuce_status)

    user_choice = choose_winner()
    game_goes_on = (user_choice != 0)
    if game_goes_on:
        scenario_id = define_scenario(user_choice, player_one, player_two, deuce_status)
        show_scores(round_num, player_one, player_two)
        return finish_round(scenario_id)
    #return enter_menu("menu_template.txt")
    return tennis()

def tennis():
    user_choice = enter_menu("menu_template.txt")
    start_new_game = ( user_choice == 1)
    if start_new_game:
        round_num = 1
        player_one = Player()
        player_two = Player()
        deuce_status = Deuce()
        return play_round(round_num, player_one, player_two, deuce_status)
    print("Goodbye")
    return 0


tennis()
