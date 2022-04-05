class Deuce:

    def __init__(self, status=False):
        self.__game_in_deuce = status

    def check(self):
        return self.__game_in_deuce

    def set_value(self, value):
        self.__game_in_deuce = value
