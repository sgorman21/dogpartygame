from action import Action


class UseAction(Action):
    def execute(self, item=None, second_item=None):
        if item is None:
            print("What should I use?")
            return 0
        for i in self.player.inventory:
            if item.lower() == i.name.lower():
                try:
                    i.use_item(second_item)
                    return 0
                except AttributeError:
                    print("This can't be used.")
                    return 0
        for j in self.player.room.inventory:
            if item.lower() == j.name.lower():
                try:
                    j.use_item(second_item)
                    return 0
                except AttributeError:
                    print("This can't be used.")
                    return 0
        print("I don't have one of those.")