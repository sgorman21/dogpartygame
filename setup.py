from playerclass import Player
from room import Room
from eataction import EatAction
from lookaction import LookAction
from takeaction import TakeAction
from dropaction import DropAction
from inventoryaction import InventoryAction
from helpaction import HelpAction
from itemclass import Item
from goaction import GoAction
from useaction import UseAction
from furnitureitem import FurnitureItem
from offaction import OffAction
from stairsitem import StairsItem
from throwableitem import ThrowableItem
from quitaction import QuitAction


def setup(name, breed):
    dogs = ["beagle", "collie", "great dane", "mutt"]
    dog_strength = [5, 10, 15, 100]
    myPlayer = None
    for i in range(4):
        if breed.lower() == dogs[i]:
            myPlayer = Player(name, None, strength=dog_strength[i], breed=dogs[i])

    # create items
    phone = Item("phone", 4, myPlayer)
    banana = Item("banana", 1, myPlayer, edible=True)
    ball = ThrowableItem("ball", 2, myPlayer)
    table = Item("table", 50, myPlayer)
    burger = Item("burger", 2, myPlayer, edible=True, accessible=False)
    chair = FurnitureItem("chair", 20, myPlayer, access_to=[burger])
    playhouse = Item("playhouse", 50, myPlayer)
    teddy = Item("teddy", 3, myPlayer)
    staircase = StairsItem("staircase", 1000, myPlayer)

    # create rooms
    hall = Room("Hall")
    landing = Room("Landing")
    garden = Room("Garden", True)
    kitchen = Room("Kitchen")
    lounge = Room("lounge")
    playroom = Room("playroom")
    bedroom = Room("bedroom")
    bathroom = Room("bathroom")
    basement = Room("basement")

    # connect rooms
    hall.connections = [kitchen, playroom, lounge, landing]
    landing.connections = [bedroom, bathroom, hall]
    garden.connections = [kitchen, basement]
    kitchen.connections = [garden, hall]
    lounge.connections = [hall]
    playroom.connections = [hall]
    bedroom.connections = [landing]
    bathroom.connections = [landing]
    basement.connections = [garden]

    staircase.access_to = [landing, hall]
    myPlayer.room = garden

    # fill rooms
    hall.inventory = [staircase, banana, phone]
    landing.inventory = [staircase, bedroom, bathroom, hall]
    garden.inventory = [chair, ball, table]
    kitchen.inventory = [chair, table, burger]
    lounge.inventory = [chair, chair, chair]
    playroom.inventory = [playhouse, teddy]
    bedroom.inventory = [teddy, phone]
    bathroom.inventory = []
    basement.inventory = []

    # create commands
    # action_string = ["eat", "look", "take", "drop", "inventory", "help_list", "go", "use", "off"]
    # action_class = [EatAction, LookAction, TakeAction, DropAction, InventoryAction, HelpAction,
    #                GoAction, UseAction, OffAction]
    # for i in range(len(action_class)):
    #    action_string[i] = action_class[i](action_string[i].capitalize, myPlayer)
    eat = EatAction("Eat", myPlayer)
    look = LookAction("Look", myPlayer)
    take = TakeAction("Take", myPlayer)
    drop = DropAction("Drop", myPlayer)
    inventory = InventoryAction("Inventory", myPlayer)
    help_list = HelpAction("Help", myPlayer)
    go = GoAction("Go", myPlayer)
    use = UseAction("Use", myPlayer)
    off = OffAction("Off", myPlayer)
    quit_game = QuitAction("Quit", myPlayer)

    # add commands to myPlayer
    myPlayer.action_list.append(eat)
    myPlayer.action_list.append(look)
    myPlayer.action_list.append(take)
    myPlayer.action_list.append(drop)
    myPlayer.action_list.append(inventory)
    myPlayer.action_list.append(help_list)
    myPlayer.action_list.append(go)
    myPlayer.action_list.append(use)
    myPlayer.action_list.append(off)
    myPlayer.action_list.append(quit_game)

    return myPlayer
