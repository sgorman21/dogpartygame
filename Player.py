class Player:
    def __init__(self, name, room, bag_contents=[], action_list=[], objective=None, strength=5,
                 on_furniture=None, breed=None, completed_objectives = []):
        self.name = name
        self.room = room
        self.bag_contents = bag_contents
        self.action_list = action_list
        self.objective = objective
        self.strength = strength
        self.on_furniture = on_furniture
        self.breed = breed
        self.completed_objectives = completed_objectives

    def execute_action(self, action_name, item=None, second_item=None):
        # See if I have an action with that name
        for action in self.action_list:
            if action.name.lower() == action_name.lower():
                if item:
                    if second_item:
                        try:
                            action.execute(item, second_item)
                            return
                        except TypeError:
                            action.execute(item)
                            return
                    else:
                        action.execute(item)
                        return
                else:
                    action.execute()
                    return
        print("What do I want to do?")
        #for j in self.room.action_list:
        #    if j.name == actionName:
        #        j.execute()