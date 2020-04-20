from reel import Reels


class Score:
    def __init__(self):
        self.reels = Reels()
        self.score = int()
        self.score_list = list()

    def set_score_list(self):
        self.score_list = [self.reels.get_reel_one(), self.reels.get_reel_two(), self.reels.get_reel_three()]

    def get_star_count(self):
        if self.score_list.count("Wild") == 1:
            return 18
        elif self.score_list.count("Star") == 3:
            return 90
        else:
            return 9

    def get_bell_count(self):
        if self.score_list.count("Wild") == 1:
            return 16
        elif self.score_list.count("Bell") == 3:
            return 80
        else:
            return 8

    def get_shell_count(self):
        if self.score_list.count("Wild") == 1:
            return 14
        elif self.score_list.count("Shell") == 3:
            return 70
        else:
            return 7

    def get_seven_count(self):
        if self.score_list.count("Wild") == 1:
            return 12
        elif self.score_list.count("Seven") == 3:
            return 60
        else:
            return 6

    def get_cherry_count(self):
        if self.score_list.count("Wild") == 1:
            return 10
        elif self.score_list.count("Cherry") == 3:
            return 50
        else:
            return 5

    def get_bar_count(self):
        if self.score_list.count("Wild") == 1:
            return 8
        elif self.score_list.count("Bar") == 3:
            return 40
        else:
            return 4

    def get_king_count(self):
        if self.score_list.count("Wild") == 1:
            return 6
        elif self.score_list.count("King") == 3:
            return 30
        else:
            return 3

    def get_queen_count(self):
        if self.score_list.count("Wild") == 1:
            return 4
        elif self.score_list.count("Queen") == 3:
            return 20
        else:
            return 2

    def get_jack_count(self):
        if self.score_list.count("Wild") == 1:
            return 2
        elif self.score_list.count("Jack") == 3:
            return 10
        else:
            return 1

    def score_count(self):
        if (self.reels.get_reel_one() != self.reels.get_reel_two() and self.reels.get_reel_one()
                != self.reels.get_reel_three() and self.reels.get_reel_two() != self.reels.get_reel_three()):
            self.score = 0
        if self.score_list.count("Wild") == 2:
            self.score = 10
        elif self.score_list.count("Wild") == 3:
            self.score = 100
        if self.score_list.count("Star") > 1:
            self.score = self.get_star_count()
        if self.score_list.count("Bell") > 1:
            self.score = self.get_bell_count()
        if self.score_list.count("Shell") > 1:
            self.score = self.get_shell_count()
        if self.score_list.count("Seven") > 1:
            self.score = self.get_seven_count()
        if self.score_list.count("Cherry") > 1:
            self.score = self.get_cherry_count()
        if self.score_list.count("Bar") > 1:
            self.score = self.get_bar_count()
        if self.score_list.count("King") > 1:
            self.score = self.get_king_count()
        if self.score_list.count("Queen") > 1:
            self.score = self.get_queen_count()
        if self.score_list.count("Jack") > 1:
            self.score = self.get_jack_count()

