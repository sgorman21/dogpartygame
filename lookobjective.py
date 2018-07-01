from objectiveclass import Objective


class LookObjective(Objective):
    def finish(self, last_command = None):
        if last_command[0].lower() is "look":
            if self.player.room.objective_list:
                self.player.objective = self.player.room.objective_list[0]
