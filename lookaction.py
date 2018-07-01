from action import Action
from helperfunctions import list_to_string


class LookAction(Action):
    def execute(self, item = None):
        print("I'm in the {0}.".format(self.player.room.name))
        if self.player.room.connections:
            rooms = "the {0}".format(self.player.room.connections[0].name.lower())
            length = len(self.player.room.connections)
            if length != 1:
                for i in range(1, length - 1):
                    rooms += ", the {0}".format(self.player.room.connections[i].name.lower())
                rooms += " and {0}".format(self.player.room.connections[length-1].name.lower())
            print("There is access to {0}.".format(rooms))
        #if len(self.player.room.inventory) == 0:
        #    print("There's nothing here...")
        #    return 0
        if self.player.room.inventory:
            #items = "A {0}".format(self.player.room.inventory[0].name.lower())
            length_inv = len(self.player.room.inventory)
            #if length_inv != 1:
            #    for j in range(1, length_inv-1):
            #        items += ", a {0}".format(self.player.room.inventory[j].name.lower())
            #    items += " and a {0}".format(self.player.room.inventory[length_inv - 1].name.lower())
            #if length_inv == 1:
            #    print("{0} is in this room.".format(items))
            #if length_inv > 1:
            #    print("{0} are in this room.".format(items))
            if length_inv == 1:
                print("A {0} is in this room.".format(self.player.room.inventory[0].name))
            else:
                print("{0} are in this room.".format(list_to_string(self.player.room.inventory, True)))
        else:
            print("There's nothing here...")
            return 0

