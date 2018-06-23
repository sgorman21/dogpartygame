class Room:
    def __init__(self, name, player_present = False, action_list = ["Look", "Take"], inventory =  [], connections = []):
        self.name = name
        self.player_present = player_present
        self.action_list = action_list
        self.inventory = inventory
        self.connections = connections
