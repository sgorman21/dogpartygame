from action import Action


class TakeAction(Action):
    def execute(self, item=None):
        if item is None:
            print("I need to choose an item to take.")
            return 0
        weight_held = 0
        for i in self.player.inventory:
            weight_held += i.weight
        for i in self.player.room.inventory:
            if i.name.lower() == item.lower():
                if i.accessible is False:
                    print("I can't get to that.")
                    return 0
                if weight_held + i.weight <= self.player.strength:
                    self.player.room.inventory.remove(i)
                    self.player.inventory.append(i)
                    print("I now have a {0}.".format(i.name))
                else:
                    print("I can't pick that up. It's too heavy.")
                return 0
        print("There is no {0} here to pick up. Maybe in a different room?".format(item))
        return 0
