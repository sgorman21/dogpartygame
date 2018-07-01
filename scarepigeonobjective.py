from objectiveclass import Objective


class ScarePigeon(Objective):
    def finish(self):
        if self.player.room.name is "garden":
            for i in self.player.room.inventory:
                if i.name == "pigeon":
                    return 0
            self.complete = True
            self.player.objective = None

