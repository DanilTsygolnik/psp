class Deuce:

    def __init__(self):
        self.__game_in_deuce = False

    def check(self):
        return self.__game_in_deuce

    def set_value(self, value):
        self.__game_in_deuce = value
