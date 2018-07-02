from action import Action
from helperfunctions import check_for_item


class DropAction(Action):
    def execute(self, item = None):
        if item is None:
            self.player.room.inventory.extend(self.player.inventory)
            self.player.inventory = []
            print("I've dropped everything.")
            return 0
        if check_for_item(item.lower(), self.player.inventory):
                self.player.inventory.remove(i)
                self.player.room.inventory.append(i)
                print("I've dropped the {0}.".format(i.name))
                return 0
        print("I'm not holding one of those.")