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
