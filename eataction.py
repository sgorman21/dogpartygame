from action import Action


class EatAction(Action):
    def execute(self, item = None):
        if item is None:
            print("What should I eat?")
            return 0
        for i in self.player.inventory:
            if item == i.name:
                if i.edible:
                    self.player.inventory.remove(i)
                    print("Yum yum yum, tasty {0}.".format(i.name))
                    return 0
                print("I can't eat that!")
                return 0
        print("I don't have that!")
