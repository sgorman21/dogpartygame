from objectiveclass import Objective
from helperfunctions import check_for_item


class TeddyObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if self.player.room.name is "playroom" and check_for_item("teddy", self.player.room.inventory):
            print("Yay! Found the teddy.")
            self.complete = True
            self.player.objective = None
            self.player.room.objective_list = self.player.room.objective_list[1:]