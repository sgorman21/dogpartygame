from itemclass import Item


class LockableItem(Item):
    def __init__(self, *args, locked=True, **kwargs):
        super(LockableItem, self).__init__(*args, **kwargs)
        self.locked = locked

    def use_item(self, second_item=None):
        if not self.locked:
            self.player.room.inventory.extend(self.access_to)
            print("There was a ")
            length_of_boyo = len(self.access_to)
            for item in self.access_to:
                print(item)

            self.access_to = []
        else:
            print("I can't get it open! Maybe it can be unlocked.")
