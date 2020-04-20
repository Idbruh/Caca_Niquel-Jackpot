from score import Score
from menu import Menu


class SlotMachine:
    def __init__(self):
        self.score_count = Score()
        self.menu = Menu()
        self.reels = self.score_count.reels

    def run_game(self):
        self.menu.score = self.score_count
        self.reels.set_reel_one()
        self.reels.set_reel_two()
        self.reels.set_reel_three()
        self.score_count.set_score_list()
        self.score_count.score_count()
        self.menu.get_score_result()


run = SlotMachine()
run.run_game()
