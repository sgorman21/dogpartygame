from itemclass import Item
from helperfunctions import list_to_string


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
