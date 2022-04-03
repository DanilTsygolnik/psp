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

def show_scores(round_num, player_one, player_two, testing=False):
    if not testing:
        print("".join( [ "==== ", "Round ", str(round_num), " score ===="]))
        print(" ".join(["Player 1 -- ", player_one.get_score()]))
        print(" ".join(["Player 2 -- ", player_two.get_score()]))
    output_str = "".join(["==== ", "Round ", str(round_num), " score ====\n",
                          "Player 1 -- ", player_one.get_score(), "\n",
                          "Player 2 -- ", player_two.get_score() 
                        ])
    return output_str

def define_scenario(user_choice, player_one, player_two, game_in_deuce):
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
            game_in_deuce = True
    if leader_score == "15":
        leader.set_score("30")
    leader.set_score("15")
    scenario_id = "Going to next round"
    return scenario_id
