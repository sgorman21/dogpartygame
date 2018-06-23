from action import Action


class InventoryAction(Action):
    def execute(self, item=None):
        for i in self.player.inventory:
            print(i.name.capitalize())
