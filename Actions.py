from Entity import Entity
from HelperFunctions import list_to_string


class Action(object):
    def __init__(self, name, player, parameters=[]):
        self.name = name
        self.parameters = parameters
        self.player = player

    def execute(self, item=None):
        raise NotImplementedError("Please implement this operation")


class EatAction(Action):
    def execute(self, item=None):
        if item is None:
            print("What should I eat?")
            return

        for heldItem in self.player.inventory:
            if item == heldItem.name:
                if heldItem.edible:
                    self.player.inventory.remove(heldItem)
                    print("Yum yum yum, tasty {0}.".format(heldItem.name))
                else:
                    print("I can't eat that!")
                return

        for room_item in self.player.room.inventory:
            if item == room_item.name:
                if room_item.edible and room_item.accessible:
                    self.player.room.inventory.remove(room_item)
                    print("Yum yum yum, tasty {0}.".format(room_item.name))
                else:
                    print("That's not something I can do.")
                return

        print("There isn't one of those here!")


class LookAction(Action):
    def execute(self, item = None):
        print("I'm in the {0}.".format(self.player.room.name))
        if self.player.room.connections:
            rooms = "the {0}".format(self.player.room.connections[0].name.lower())
            length = len(self.player.room.connections)
            if length != 1:
                for counter in range(1, length - 1):
                    rooms += ", the {0}".format(self.player.room.connections[counter].name.lower())
                rooms += " and {0}".format(self.player.room.connections[length-1].name.lower())
            print("There is access to {0}.".format(list_to_string(self.player.room.connections, article=True, article_definite=True))) # testing
        if self.player.room.inventory:
            length_inv = len(self.player.room.inventory)
            if length_inv == 1:
                print("A {0} is in this room.".format(self.player.room.inventory[0].name))
            else:
                print("{0} are in this room.".format(list_to_string(self.player.room.inventory, True)))
        else:
            print("There's nothing here...")
            return 0


class TakeAction(Action):
    def execute(self, item=None):
        if item is None:
            print("I need to choose an item to take.")
            return 0
        weight_held = 0
        for item in self.player.inventory:
            weight_held += item.weight
        for item in self.player.room.inventory:
            if item.name.lower() == item.lower():
                if item.accessible is False:
                    print("I can't get to that.")
                    return 0
                if weight_held + item.weight <= self.player.strength:
                    self.player.room.inventory.remove(item)
                    self.player.inventory.append(item)
                    print("I now have a {0}.".format(item.name))
                else:
                    print("I can't pick that up. It's too heavy.")
                return 0
        print("There is no {0} here to pick up. Maybe in a different room?".format(item))
        return 0


class DropAction(Action):
    def execute(self, item=None):
        if item is None:
            self.player.room.inventory.extend(self.player.inventory)
            self.player.inventory = []
            print("I've dropped everything.")
            return

        for inventoryItem in self.player.inventory:
            if item.lower() == inventoryItem.name:
                self.player.inventory.remove(inventoryItem)
                self.player.room.inventory.append(inventoryItem)
                print("I've dropped the {0}.".format(inventoryItem.name))
                return
        print("I'm not holding one of those.")


class InventoryAction(Action):
    def execute(self, item=None):
        for heldItem in self.player.inventory:
            print(heldItem.name.capitalize())


class HelpAction(Action):
    def execute(self, item=None):
        #action_list = self.player.action_list

        #actions = "{0}".format(action_list[0].name.lower())

        #for i in range(1, len(action_list) - 1):
        #    actions += ", {0}".format(action_list[i].name.lower())

        #actions += " and {0}.".format(action_list[-1].name.lower())

        #include_articles = True
        #sentence_case = False

        #output = ''
        #list_size = len(action_list)
        # just for fun
        #for i in range(list_size):
        #    output += (', ' if 0 < i < list_size - 1 else 'and ') + \
        #              (('A ' if i == 0 and sentence_case else 'a ') if include_articles else '') + action_list[i]

        print("The possible actions are {0}.".format(list_to_string(self.player.action_list, False, False)))


class GoAction(Action):
    def execute(self, destination=None):
        if destination is None:
            print("Where should I go?")
            return

        if destination.lower() == self.player.room.name:
            print("I'm already here!")
            return

        for connectedRoom in self.player.room.connections:
            if destination.lower() == connectedRoom.name.lower():
                if not self.player.on_furniture:
                    self.player.room = connectedRoom
                    self.player.room.player_present = False
                    connectedRoom.player_present = True
                    return
                print("I'm on a {0}! I need to get off.".format(self.player.on_furniture.name))

        print("I can't go there.")


class UseAction(Action):
    def execute(self, item=None, second_item=None):
        if item is None:
            print("What should I use?")
            return 0
        for heldItem in self.player.inventory:
            if item.lower() == heldItem.name.lower():
                try:
                    heldItem.use_item(second_item)
                    return 0
                except AttributeError:
                    print("This can't be used.")
                    return 0
        for roomItem in self.player.room.inventory:
            if item.lower() == roomItem.name.lower():
                try:
                    roomItem.use_item(second_item)
                    return 0
                except AttributeError:
                    print("This can't be used.")
                    return 0
        print("I don't have one of those.")


class BarkAction(Action):
    def execute(self, item=None):
        if item is not None:
            print("I can't bark words! I'm a dog!")
            return

        something_gone = False
        for heldItem in self.player.room.inventory:
            if type(heldItem) is Entity and heldItem.skittish:
                    self.player.room.inventory.remove(heldItem)
                    print("The {0} has gone!".format(heldItem.name))
                    something_gone = True
        if not something_gone:
                print("Nothing was scared of my fearsome bark.")


class OffAction(Action):
    def execute(self, item=None):
        if not self.player.on_furniture:
            print("I'm not on anything to get off.")
            return 0
        print("I'm off the {0} now.".format(self.player.on_furniture.name))
        for itemToBeAccessed in self.player.on_furniture.access_to:
            if itemToBeAccessed in self.player.room.inventory:
                itemToBeAccessed.accessible = False
        self.player.on_furniture = None


class AimAction(Action):
    def execute(self, item=None):
        print(self.player.objective.description)


class QuitAction(Action):
    def execute(self, item=None):
        exit(0)