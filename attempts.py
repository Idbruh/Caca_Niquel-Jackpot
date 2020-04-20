def set_score(self):
    # score 0
    if self.__reel1 != self.__reel2 and self.__reel1 != self.__reel3 and self.__reel2 != self.__reel3:
        self.score = 0
    # wild
    elif self.__reel1 == self.__reel2:
        if self.__reel1 == "Wild" and self.__reel3 == "Wild":
            self.score = 100
        elif self.__reel1 == "Wild":
            self.score = 10
    # star

    ________________________________________________________________________________________________________________

from reel import Reels


class Score:
    def __init__(self):
        self.reels = Reels()
        self.score = int()
        self.score_list = list()

    def set_score_list(self):
        self.score_list = [self.reels.get_reel_one(), self.reels.get_reel_two(), self.reels.get_reel_three()]

    def score_count(self):
        if (self.reels.get_reel_one() != self.reels.get_reel_two() and self.reels.get_reel_one()
                != self.reels.get_reel_three() and self.reels.get_reel_two() != self.reels.get_reel_three()):
            self.score = 0
        # wild
        if self.score_list.count("Wild") == 2:
            self.score = 10
        elif self.score_list.count("Wild") == 3:
            self.score = 100
        # star
        if self.score_list.count("Star") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 18
            elif self.score_list.count("Star") == 3:
                self.score = 90
            else:
                self.score = 9
        # Bell
        if self.score_list.count("Bell") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 16
            elif self.score_list.count("Bell") == 3:
                self.score = 80
            else:
                self.score = 8
        # Shell
        if self.score_list.count("Shell") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 14
            elif self.score_list.count("Shell") == 3:
                self.score = 70
            else:
                self.score = 7
        # Seven
        if self.score_list.count("Seven") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 12
            elif self.score_list.count("Seven") == 3:
                self.score = 60
            else:
                self.score = 6
        # Cherry
        if self.score_list.count("Cherry") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 10
            elif self.score_list.count("Cherry") == 3:
                self.score = 50
            else:
                self.score = 5
        # Bar
        if self.score_list.count("Bar") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 8
            elif self.score_list.count("Bar") == 3:
                self.score = 40
            else:
                self.score = 4
        # King
        if self.score_list.count("King") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 6
            elif self.score_list.count("King") == 3:
                self.score = 30
            else:
                self.score = 3
        # Queen
        if self.score_list.count("Queen") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 4
            elif self.score_list.count("Queen") == 3:
                self.score = 20
            else:
                self.score = 2
        # Jack
        if self.score_list.count("Jack") > 1:
            if self.score_list.count("Wild") == 1:
                self.score = 2
            elif self.score_list.count("Jack") == 3:
                self.score = 10
            else:
                self.score = 1

