from action import Action
from helperfunctions import check_for_item


class EatAction(Action):
    def execute(self, item=None):
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
        for j in self.player.room.inventory:
            if item == j.name:
                if j.edible and j.accessible:
                    self.player.room.inventory.remove(j)
                    print("Yum yum yum, tasty {0}.".format(j.name))
                    return 0
                else:
                    print(" That's not something I can do.")
                    return 0
        print("There isn't one of those here!")
