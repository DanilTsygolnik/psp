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

def update_score(user_choice, player_one, player_two):
    player_one_wins = (user_choice == 1)
    if player_one_wins:
        player_one.add_point()
        return 1
    player_two.add_point()
    return 2
