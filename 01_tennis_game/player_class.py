class Player:

    def __init__(self, init_points:str="love"):
        self.__score = init_points
        self.__has_advantage = False

    def set_score(self, points):
        self.__score = points

    def get_score(self):
        return self.__score

    def add_advantage(self):
        self.__has_advantage = True

    def remove_advantage(self):
        self.__has_advantage = False

    def check_advantage(self):
        return self.__has_advantage
