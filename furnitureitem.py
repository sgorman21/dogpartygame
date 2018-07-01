from itemclass import Item


class FurnitureItem(Item):
    def use_item(self, second_item=None):
        for i in self.player.room.inventory:
            if self.name.lower() == i.name.lower():
                self.player.on_furniture = self
                print("I'm on the {0} now.".format(self.name))
                for j in self.access_to:
                    j.accessible = True
                    print(j.name, j.accessible)
                return 0
        print("I'm holding that. I should drop it first.")
