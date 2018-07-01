class Objective:
    def __init__(self, player, description = None, complete=False):
        self.player = player
        self.description = description
        self.complete = complete

    def finish(self, last_command=None):
        self.complete = True
        self.player.objective = None
