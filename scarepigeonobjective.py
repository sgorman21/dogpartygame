from objectiveclass import Objective
from entityclass import Entity


class ScarePigeon(Objective):
    def start(self, last_command):
        pigeon = Entity("pigeon", self.player, skittish=True)
        self.player.room.inventory.append(pigeon)

    def finish(self, last_command):
        if self.player.room.name is "garden":
            for i in self.player.room.inventory:
                if i.name == "pigeon":
                    return 0
            self.complete = True
            self.player.objective = None
            self.player.room.objective_list = self.player.room.objective_list[1:]

