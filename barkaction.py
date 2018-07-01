from action import Action
from entityclass import Entity
from itemclass import Item


class BarkAction(Action):
    def execute(self, item=None):
        if item is not None:
            print("I can't bark words! I'm a dog!")
        else:
            something_gone = False
            for i in self.player.room.inventory:
                if type(i) is Entity:
                    if i.skittish:
                        self.player.room.inventory.remove(i)
                        print("The {0} has gone!".format(i.name))
                        something_gone = True
            if not something_gone:
                    print("Nothing was scared of my fearsome bark.")
