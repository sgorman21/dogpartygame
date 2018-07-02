from objectiveclass import Objective
from entityclass import Entity
from helperfunctions import check_for_item


class ScarePigeon(Objective):
    def start(self, last_command):
        pigeon = Entity("pigeon", self.player, skittish=True)
        self.player.room.inventory.append(pigeon)

    def finish(self, last_command):
        if self.player.room.name is "garden":
            if check_for_item("pigeon", self.player.room.inventory):
                return 0
            self.complete = True
            self.player.objective = None
            self.player.room.objective_list = self.player.room.objective_list[1:]
            print("The food is safe! Good job me.")

