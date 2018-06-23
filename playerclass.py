class Player:
    def __init__(self, name, room, inventory=[], action_list=[], strength=5, on_furniture=None, breed=None):
        self.name = name
        self.room = room
        self.inventory = inventory
        self.action_list = action_list
        self.strength = strength
        self.on_furniture = on_furniture
        self.breed = breed

    def execute_action(self, action_name, item=None):
        # See if I have an action with that name
        for i in self.action_list:
            if i.name.lower() == action_name.lower():
                i.execute(item)
                return 0
        print("What do I want to do?")
        #for j in self.room.action_list:
        #    if j.name == actionName:
        #        j.execute()