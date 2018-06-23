from action import Action


class DropAction(Action):
    def execute(self, item = None):
        if item is None:
            self.player.room.inventory.extend(self.player.inventory)
            self.player.inventory = []
            print("I've dropped everything.")
            return 0
        for i in self.player.inventory:
            if item.lower() == i.name:
                self.player.inventory.remove(i)
                self.player.room.inventory.append(i)
                print("I've dropped the {0}.".format(i.name))
                return 0
        print("I'm not holding one of those.")