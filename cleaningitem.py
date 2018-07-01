from itemclass import Item


class CleaningItem(Item):
    def use_item(self, second_item=None):
        for i in self.player.room.inventory:
            if i.name in ["juice"]:
                self.player.room.inventory.remove(i)