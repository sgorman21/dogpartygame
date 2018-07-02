from entityclass import Entity


class Action(object):
    def __init__(self, name, player, parameters=[]):
        self.name = name
        self.parameters = parameters
        self.player = player

    def execute(self, item=None):
        raise NotImplementedError("Please implement this operation")


class BarkAction(Action):
    def execute(self, item=None):
        if item is not None:
            print("I can't bark words! I'm a dog!")
            return

        something_gone = False
        for i in self.player.room.inventory:
            if type(i) is Entity and i.skittish:
                    self.player.room.inventory.remove(i)
                    print("The {0} has gone!".format(i.name))
                    something_gone = True
        if not something_gone:
                print("Nothing was scared of my fearsome bark.")


class EatAction(Action):
    def execute(self, item=None):
        if item is None:
            print("What should I eat?")
            return

        for i in self.player.inventory:
            if item == i.name:
                if i.edible:
                    self.player.inventory.remove(i)
                    print("Yum yum yum, tasty {0}.".format(i.name))
                else:
                    print("I can't eat that!")
                return

        for j in self.player.room.inventory:
            if item == j.name:
                if j.edible and j.accessible:
                    self.player.room.inventory.remove(j)
                    print("Yum yum yum, tasty {0}.".format(j.name))
                else:
                    print("That's not something I can do.")
                return

        print("There isn't one of those here!")


class GoAction(Action):
    def execute(self, destination=None):
        if destination is None:
            print("Where should I go?")
            return

        if destination.lower() == self.player.room.name:
            print("I'm already here!")
            return

        for r in self.player.room.connections:
            if destination.lower() == r.name.lower():
                if not self.player.on_furniture:
                    self.player.room = r
                    self.player.room.player_present = False
                    r.player_present = True
                    return
                print("I'm on a {0}! I need to get off.".format(self.player.on_furniture.name))

        print("I can't go there.")


class HelpAction(Action):
    def execute(self, item=None):
        action_list = self.player.action_list

        actions = "{0}".format(action_list[0].name.lower())

        for i in range(1, len(action_list) - 1):
            actions += ", {0}".format(action_list[i].name.lower())

        actions += " and {0}.".format(action_list[:-1].name.lower())

        include_articles = True
        sentence_case = False

        output = ''
        list_size = len(action_list)
        # just for fun
        for i in range(list_size):
            output += (', ' if 0 < i < list_size - 1 else 'and ') + \
                      (('A ' if i == 0 and sentence_case else 'a ') if include_articles else '') + action_list[i]

        print("The possible actions are {0}".format(actions))


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
