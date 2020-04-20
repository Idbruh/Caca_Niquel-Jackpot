from score import Score


class Menu:
    def __init__(self):
        self.score = Score()

    def get_score_result(self):
        print(f'''
                  YOUR SCORE IS: {self.score.score}

                      .-------.
                      |Jackpot|
          ____________|_______|____________
         |  __    __    ___  _____   __    |  
         | / _\  / /   /___\/__   \ / _\   | 
         | \ \  / /   //  //  / /\ \\ \    |  
         | _\ \/ /___/ \_//  / /  \/_\ \   | 
         | \__/\____/\___/   \/     \__/   |
         |===_______===_______===_______===|

             {self.score.reels.get_reel_one()} *||* {self.score.reels.get_reel_two()} *||* {self.score.reels.get_reel_three()} 
      
         |===_______===_______===_______===|
         |  /___________________________\  |
         |   |                         |   |
        _|    \_______________________/    |_
        (____________________________________)


                ''')
