from Entity import Entity
from HelperFunctions import list_to_string
from HelperFunctions import calculate_weight
from Setup import *


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
    def execute(self, item=None):
        #global connections_list
        #print("I'm in the {0}.".format(self.player.room.name))
        #current_connections = []
        #for possible_connection in connections_list:
        #    if self.player.room in possible_connection:
        #        current_connections.append(possible_connection)
        #if len(current_connections) == 0:
        #    print("I can't go anywhere. I'm stuck in here...")
        #else:
        #    print("There is access to {0}".format(list_to_string(current_connections, article_definite=True)))

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
        #weight_held = 0
        #for item in self.player.inventory:
        #    weight_held += item.weight
        for held_item in self.player.room.inventory:
            if held_item.name.lower() == item.lower():
                if held_item.accessible is False:
                    print("I can't get to that.")
                    return 0
                if calculate_weight(self.player.inventory) + held_item.weight <= self.player.strength:
                    self.player.room.inventory.remove(held_item)
                    self.player.inventory.append(held_item)
                    print("I now have a {0}.".format(held_item.name))
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
        for inventoryItem in self.player.inventory:
            try:
                if inventoryItem.capacity != 0 and inventoryItem.accessto:
                    for item_in_item in inventoryItem.accessto:
                        if item.lower() == item_in_item.name:
                            inventoryItem.accessto.remove(item_in_item)
                            self.player.room.inventory.append(item_in_item)
                            print("I've dropped the {0}.".format(item_in_item.name))
                            return
            except AttributeError:
                pass
                    
        print("I'm not holding one of those.")


class InventoryAction(Action):
    def execute(self, item=None):
        for heldItem in self.player.inventory:
            print(heldItem.name.capitalize())
        for inventoryItem in self.player.inventory:
            try:
                if inventoryItem.capacity != 0 and inventoryItem.access_to:
                    print("Inside the {0} I have {1}.".format(inventoryItem, list_to_string(inventoryItem.access_to)))
            except AttributeError:
                print("This has no storage.")
        if not self.player.inventory:
            print("I'm not holding anything.")


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
    def execute(self, wanted_destination=None):
        if wanted_destination is None:
            print("Where should I go?")
            return

        #destination = None
        #for room in room_list:
        #    if room.name == wanted_destination:
        #        destination = room
        #    if destination is None:
        #        print("There isn't anywhere called that.")
        #        return

        if wanted_destination.lower() == self.player.room.name:
            print("I'm already here!")
            return
        # if destination.lower() == self.player.room.name:
        #     print("I'm already here!")
        #     return

        #if check_connection(self.player.room, destination):
        #    if not self.player.on_furniture:
        #        self.player.room = destination
        #        self.player.room.player_present = False
        #        destination.player_present = True
        #        return
        #    print("I'm on a {0}! I need to get off.".format(self.player.on_furniture.name))
        for connectedRoom in self.player.room.connections:
            if wanted_destination.lower() == connectedRoom.name.lower():
                if not self.player.on_furniture:
                    self.player.room = connectedRoom
                    self.player.room.player_present = False
                    connectedRoom.player_present = True
                    print("I'm now in the {0}.".format(self.player.room.name))
                    return
                print("I'm on a {0}! I need to get off.".format(self.player.on_furniture.name))
                return

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


class StoreAction(Action):
    def execute(self, item=None):
        carrier_present = False
        is_item = False
        for players_item in self.player.inventory:
            if players_item.name == item.lower():
                item = players_item
                is_item = True
                break
        if not is_item:
            print("I don't have one of those to store.")
            return
        for held_item in self.player.inventory:
            try:
                if calculate_weight(held_item.access_to) <= held_item.capacity - item.weight:
                    held_item.access_to.append(item)
                    self.player.inventory.remove(item)
                    print("The {0} has been stored in {1}.".format(item.name, held_item.name))
                    return
                carrier_present = True
            except AttributeError:
                pass
        if carrier_present:
            print("There isn't enough room left to store this.")
        else:
            print("I don't have anywhere to store this.")
            print("I don't have anywhere to store this.")


class DestroyAction(Action):
    def execute(self, item=None):
        success = False
        for held_item in self.player.inventory:
            if item.lower() == held_item.name:
                self.player.inventory.remove(held_item)
                print("The {0} is broken to pieces! Mwhahaha.".format(held_item.name))
                success = True
                for hidden_item in held_item.access_to:
                    self.player.room.inventory.append(hidden_item)
                    if len(held_item.access_to) == 1:
                        print("A {0} was in the {1}.".format(held_item.access_to[0], held_item.name))
                    elif len(held_item.access_to) > 1:
                        print("{0} were in the {1}.".format(list_to_string(held_item.access_to, capital=True)), held_item.name)
        if not success:
            print("I don't have one of those to destroy. Maybe I can find one...")