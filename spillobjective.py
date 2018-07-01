from objectiveclass import Objective
from itemclass import Item


class SpillObjective(Objective):
    def start(self, last_command):
        juice = Item("juice", 0, self.player, accessible=False, edible=True)
        self.player.room.inventory.append(juice)

    def finish(self, last_command):
        if self.player.room.name is "kitchen":
            juice_here = False
            for i in self.player.room.inventory:
                if i.name is "juice":
                    juice_here = True
            if not juice_here:
                print("Nice and tidy.")
                self.complete = True
                self.player.objective = None
                self.player.room.objective_list = self.player.room.objective_list[1:]
