from objectiveclass import Objective


class LookObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if last_command[0].lower() == 'look' and self.player.objective is not None:
            if self.player.room.objective_list:
                self.player.objective = self.player.room.objective_list[0]
                self.player.objective.start(last_command)
                print(self.player.objective.description)
