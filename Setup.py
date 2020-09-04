from Player import Player
from Items import *
from Objectives import *
from Actions import *
from Room import Room


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
    chair = FurnitureItem("chair", 20, myPlayer)
    playhouse = Item("playhouse", 50, myPlayer)
    teddy = Item("teddy", 3, myPlayer)
    staircase = StairsItem("staircase", 1000, myPlayer)
    toybox = LockableItem("toybox", 50, myPlayer, access_to=[teddy])
    key = KeyItem("key", 2, myPlayer, access_to=[toybox])
    tissue = CleaningItem("tissue", 1, myPlayer)

    # create rooms
    hall = Room("hall")
    landing = Room("landing")
    garden = Room("garden", True)
    kitchen = Room("kitchen")
    lounge = Room("lounge")
    playroom = Room("playroom")
    bedroom = Room("bedroom")
    bathroom = Room("bathroom")
    basement = Room("basement")


    # connect rooms
    #add_connection(kitchen, garden)
    #add_connection(kitchen, hall)
    #add_connection(hall, lounge)
    #add_connection(hall, playroom)
    #add_connection(hall, landing)
    #add_connection(landing, bedroom)
    #add_connection(landing, bathroom)

    hall.connections = [kitchen, playroom, lounge, landing]
    landing.connections = [bedroom, bathroom, hall]
    garden.connections = [kitchen]
    kitchen.connections = [garden, hall]
    lounge.connections = [hall]
    playroom.connections = [hall]
    bedroom.connections = [landing]
    bathroom.connections = [landing]

    staircase.access_to = [landing, hall]
    myPlayer.room = garden

    # fill rooms
    hall.inventory = [staircase, banana, phone]
    landing.inventory = [staircase, bedroom, bathroom, hall]
    garden.inventory = [chair, ball, table, toybox]
    kitchen.inventory = [chair, table]
    lounge.inventory = [chair, chair, chair, key]
    playroom.inventory = [playhouse, toybox]
    bedroom.inventory = [phone]
    bathroom.inventory = [tissue]


    # objectives
    look_objective = LookObjective(myPlayer, description="Look around to find something to do.")
    scare_pigeon = ScarePigeon(myPlayer, description="I need to scare away the pigeon before it eats the food.")
    eat_burger = EatBurger(myPlayer, description="I'd really like that burger on the bench by that chair...")
    find_teddy = TeddyObjective(myPlayer, description="I want a cuddle. I wonder if there's anything in that toybox...")
    spill_juice = SpillObjective(myPlayer, description="Oh no! Someone spilt some juice. "
                                                       "There's got to be some way to clean it up.")
    open_basement = OpenBasement(myPlayer, description="I've noticed a trapdoor beside the backdoor."
                                                       " I wonder what's through it...", prerequisites=["SpillObjective"])


    # objectives in rooms
    garden.objective_list = [scare_pigeon, open_basement]
    kitchen.objective_list = [eat_burger, spill_juice]
    playroom.objective_list = [find_teddy]


    # create commands
    # action_string = ["eat", "look", "take", "drop", "inventory", "help_list", "go", "use", "off"]
    # action_class = [EatAction, LookAction, TakeAction, DropAction, InventoryAction, HelpAction,
    #                GoAction, UseAction, OffAction]
    # for i in range(len(action_class)):
    #    action_string[i] = action_class[i](action_string[i].capitalize, myPlayer)
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


    # add commands to myPlayer
    myPlayer.action_list.append(eat)
    myPlayer.action_list.append(look)
    myPlayer.action_list.append(take)
    myPlayer.action_list.append(drop)
    myPlayer.action_list.append(inventory)
    myPlayer.action_list.append(help_list)
    myPlayer.action_list.append(go)
    myPlayer.action_list.append(use)
    myPlayer.action_list.append(bark)
    myPlayer.action_list.append(off)
    myPlayer.action_list.append(aim)
    myPlayer.action_list.append(quit_game)
    myPlayer.action_list.append(store)
    myPlayer.action_list.append(destroy)

    myPlayer.objective = look_objective

    return myPlayer
