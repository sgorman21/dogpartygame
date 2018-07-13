from HelperFunctions import list_to_string
from Actions import GoAction


class Item:
    def __init__(self, name, weight, player, edible=False, accessible=True, access_to=[]):
        self.name = name
        self.weight = weight
        self.player = player
        self.edible = edible
        self.accessible = accessible
        self.access_to = access_to

    def __str__(self):
        return self.name

    def use_item(self, second_item=None):
        print("This item can't be used.")


class CleaningItem(Item):
    def use_item(self, second_item=None):
        for i in self.player.room.inventory:
            if i.name in ["juice"]:
                self.player.room.inventory.remove(i)


class FurnitureItem(Item):
    def use_item(self, second_item=None):
        for i in self.player.room.inventory:
            if self.player.on_furniture is True:
                print("I'm already on something!")
                return 0
            if self.name.lower() == i.name.lower():
                self.player.on_furniture = self
                print("I'm on the {0} now.".format(self.name))
                for j in self.player.room.inventory:
                    if j in self.access_to:
                        j.accessible = True
                return 0
        print("I'm holding that. I should drop it first.")


class LockableItem(Item):
    def __init__(self, *args, locked=True, **kwargs):
        super(LockableItem, self).__init__(*args, **kwargs)
        self.locked = locked

    def use_item(self, second_item=None):
        if not self.locked:
            self.player.room.inventory.extend(self.access_to)
            if len(self.access_to) >= 1:
                if len(self.access_to) == 1:
                    print("A {0} was emptied into the room.".format(self.access_to[0].name))
                else:
                    print("{0} were emptied into the room.".format(list_to_string(self.access_to, True)))
            else:
                print("There wasn't anything in there...")
            self.access_to = []
        else:
            print("I can't get it open! Maybe it can be unlocked.")


class KeyItem(Item):
    def use_item(self, second_item=None):
        unlock_item = None
        for item in self.player.room.inventory:
            if second_item.lower() == item.name:
                unlock_item = item
        if type(unlock_item) is LockableItem:
            if unlock_item.locked and unlock_item.accessible and unlock_item in self.access_to:
                unlock_item.locked = False
                print("The {0} is open!".format(unlock_item.name))
            else:
                print("I can't unlock that.")
        else:
            print("There's no lock there.")


class StairsItem(Item):
    def use_item(self, second_item=None):
        go = GoAction("go", self.player)
        for i in self.access_to:
            if not self.player.room.name.lower() == i.name.lower():
                go.execute(wanted_destination= i.name)
                return
        print("These stairs can't get me anywhere.")


class ThrowableItem(Item):
    def use_item(self, second_item=None):
        print("Look at it go!")
        self.player.inventory.remove(self)
        self.player.room.inventory.append(self)


class CarrierItem(Item):
    def __init__(self, *args, capacity=0, **kwargs):
        super(CarrierItem, self).__init__(*args, **kwargs)
        self.capacity = capacity

    def use_item(self, second_item=None):
        print("To use a storage item try using the store command")


class BreakableItem(Item):
    def use_item(self, second_item=None):
        print("The {0} has broken and dropped {1}.".format(self.name, list_to_string(self.access_to)))
        self.player.room.remove(self)
        for hidden_item in self.access_to:
            self.player.room.inventory.append(hidden_item)
        return