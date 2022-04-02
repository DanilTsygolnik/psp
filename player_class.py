class Player:

    def __init__(self):
        self.__score = 0
        self.__has_advantage = False

    def add_point(self):
        self.__score += 1

    def get_score(self):
        return self.__score

    def add_advantage(self):
        self.__has_advantage = True

    def remove_advantage(self):
        self.__has_advantage = False

    def check_advantage(self):
        return self.__has_advantage
