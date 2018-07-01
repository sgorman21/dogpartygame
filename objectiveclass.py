class Objective:
    def __init__(self, player, description="There isn't anything more to do in this room.", complete=False):
        self.player = player
        self.description = description
        self.complete = complete

    def start(self, last_command):
        self.complete = False

    def finish(self, last_command):
        self.complete = True
        self.player.objective = None
