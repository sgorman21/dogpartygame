import os
import sys

from Actions import Action
from Setup import setup


class RestartAction(Action):
    def execute(self, item=None):

        print("Game Over.")

        yeses = ["y", "yes", 1]
        noes = ["n", "no", 0]

        while True:
            response = input("Do you want to restart?\n>")
            if response in noes:
                return
            elif response in yeses:
                os.execl(sys.executable, sys.executable, *sys.argv)
            print("Valid options, y or n")
# TODO restart doesn't work but may be PyCharm
