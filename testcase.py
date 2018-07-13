from Setup import *
from Restart import RestartAction
from Intro import intro
from Objectives import LookObjective
import inspect
from pprint import pprint

garden = Room("garden", True)
myPlayer = Player("Me", garden, [])
open_basement = OpenBasement(myPlayer, description="I've noticed a trapdoor beside the backdoor."
                                                       " I wonder what's through it...")
garden.objective_list = [open_basement]

eat = EatAction("eat", myPlayer)
look = LookAction("look", myPlayer)
take = TakeAction("take", myPlayer)
drop = DropAction("drop", myPlayer)
inventory = InventoryAction("inventory", myPlayer)
help_list = HelpAction("help", myPlayer)
go = GoAction("go", myPlayer)
use = UseAction("use", myPlayer)
bark = BarkAction("bark", myPlayer)
off = OffAction("off", myPlayer)
aim = AimAction("aim", myPlayer)
quit_game = QuitAction("quit", myPlayer)
store = StoreAction("store", myPlayer)
destroy = DestroyAction("destroy", myPlayer)

myPlayer.action_list = [eat, look, take, drop, inventory, use, quit_game, store, destroy, go]
look_objective = LookObjective(myPlayer, description="Look around to find something to do.")
myPlayer.objective = look_objective

while True:
    myActionText = input(">")
    myActionText = myActionText.split()
    if len(myActionText) == 1:
        myPlayer.execute_action(myActionText[0])
    if len(myActionText) == 2:
        myPlayer.execute_action(myActionText[0], myActionText[1])
    if len(myActionText) > 2:
        myPlayer.execute_action(myActionText[0], myActionText[1], myActionText[2])
    myPlayer.objective.finish(last_command=myActionText)
    if myPlayer.objective is None:
        myPlayer.objective = LookObjective(myPlayer)
    #for i in myPlayer.room.inventory:
    #    if i.name == "trapdoor":
    #        pprint(vars(i))
