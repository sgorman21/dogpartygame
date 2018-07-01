from objectiveclass import Objective


class TeddyObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if self.player.room.name is "playroom" and self.player.room.inventory[len(self.player.room.inventory)-1].name is "teddy":
            print("Yay! Found the teddy.")
            self.complete = True
            self.player.objective = None
            self.player.room.objective_list = self.player.room.objective_list[1:]