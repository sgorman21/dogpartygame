from itemclass import Item


class ThrowableItem(Item):
    def use_item(self, second_item=None):
        print("Look at it go!")
        self.player.inventory.remove(self)
        self.player.room.inventory.append(self)
