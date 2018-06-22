from action import Action
from setup import setup


class RestartAction(Action):
    def execute(self, item=None):
        yeses = ["y", "yes", 1]
        noes = ["n", "no", 0]
        print("Game Over.")
        response = input("Do you want to restart?\n>")
        if response in noes:
            print("Ok!")
            return 0
        if response in yeses:
            chosen_name = self.player.name
            chosen_breed = self.player.breed
            self.player = None
            # self.player = setup(chosen_name, chosen_breed)
            print("success")
            return 0
        print("Please respond yes or no.\n>")
