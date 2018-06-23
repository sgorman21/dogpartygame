from action import Action


class OffAction(Action):
    def execute(self, item=None):
        if not self.player.on_furniture:
            print("I'm not on anything to get off.")
            return 0
        print("I'm off the {0} now.".format(self.player.on_furniture.name))
        for i in self.player.on_furniture.access_to:
            if i in self.player.room.inventory:
                i.accessible = False
        self.player.on_furniture = None
