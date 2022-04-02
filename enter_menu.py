def print_menu(menu_templ_file):
    with open(menu_templ_file, 'r') as file:
        for line in file:
            print(line.strip())

def get_user_choice():
    print("Please enter the number: ")
    user_choice = str(input())
    if user_choice == "1":
        return 1
    if user_choice == "0":
        return 0
    print("Wrong input. Please try again.")
    return get_user_choice()

def enter_menu(menu_templ_file):
    print_menu(menu_templ_file)
    return get_user_choice()
