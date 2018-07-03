class Room:
    def __init__(self, name, player_present=False, action_list=["Look", "Take"], inventory=[], connections=[], objective_list=[]):
        self.name = name
        self.player_present = player_present
        self.action_list = action_list
        self.inventory = inventory
        self.connections = connections
        self.objective_list = objective_list
