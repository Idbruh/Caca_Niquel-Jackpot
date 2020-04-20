from random import choice

class Reels:
    def __init__(self):
        self.__reel = ["Wild", "Star", "Bell", "Shell", "Seven", "Cherry", "Bar", "King", "Queen", "Jack"]
        self.__reel1 = str()
        self.__reel2 = str()
        self.__reel3 = str()

    def get_reel_one(self):
        reel1 = self.__reel1
        return reel1

    def get_reel_two(self):
        reel2 = self.__reel2
        return reel2

    def get_reel_three(self):
        reel3 = self.__reel3
        return reel3

    def set_reel_one(self):
        self.__reel1 = choice(self.__reel)

    def set_reel_two(self):
        self.__reel2 = choice(self.__reel)

    def set_reel_three(self):
        self.__reel3 = choice(self.__reel)




