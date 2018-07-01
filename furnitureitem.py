from itemclass import Item


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
