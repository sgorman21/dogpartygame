from objectiveclass import Objective
from itemclass import Item


class EatBurger(Objective):
    def start(self, last_command):
        if self.player.room.name is 'kitchen':
            burger_here = False
            for i in self.player.room.inventory:
                if i.name == "burger":
                    burger_here = True
            if not burger_here:
                burger = Item("burger", 2, self.player, edible= True, accessible=False)
                self.player.room.inventory.append(burger)

    def finish(self, last_command):
        if self.player.room.name is "kitchen":
            if last_command[0].lower() == 'eat' and last_command[1].lower() == 'burger':
                print("Mmm, that was nice. What next?")
                self.complete = True
                self.player.objective = None
                self.player.room.objective_list = self.player.room.objective_list[1:]