from action import Action


class AimAction(Action):
    def execute(self, item=None):
        print(self.player.objective.description)