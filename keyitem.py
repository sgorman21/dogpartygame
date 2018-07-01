from itemclass import Item
from lockableitem import LockableItem


class KeyItem(Item):
    def use_item(self, second_item=None):
        for i in self.player.room.inventory:
            if second_item.lower() == i.name:
                second_item = i
        if type(second_item) is LockableItem:
            if second_item.locked and second_item.accessible and second_item in self.access_to:
                second_item.locked = False
                print("The {0} is open!".format(second_item.name))
            else:
                print("I can't unlock that.")
        else:
            print("There's no lock there.")
