from furnitureitem import FurnitureItem
from useaction import UseAction
from itemclass import Item
from room import Room
from playerclass import Player
from takeaction import TakeAction

banana = Item("banana", 1, edible=True)
burger = Item("burger", 2, edible=True, accessible=False)
chair = FurnitureItem("chair", 20, access_to= burger)
garden = Room("Garden", True, ["Look", "Take"], [chair, burger, banana])

myPlayer = Player("me", garden, inventory=[banana], strength=5)
use = UseAction("Use", myPlayer)
take = TakeAction("Take", myPlayer)
myPlayer.action_list = [use, take]

print(chair.use_item())
