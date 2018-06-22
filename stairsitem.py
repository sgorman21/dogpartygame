from itemclass import Item
from goaction import GoAction


class StairsItem(Item):
    def use_item(self, second_item=None):
        go = GoAction("go", self.player)
        for i in self.access_to:
            if not self.player.room.name.lower() == i.name.lower():
                go.execute(item = i.name)
                return 0
        print("These stairs can't get me anywhere")