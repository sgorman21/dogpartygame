class Action:
    def __init__(self, name, player, parameters=[]):
        self.name = name
        self.parameters = parameters
        self.player = player

    def execute(self, item=None):
        raise NotImplementedError("Please implement this operation")
