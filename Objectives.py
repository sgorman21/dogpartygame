from Items import *
from HelperFunctions import *
from Entity import Entity


class Objective:
    def __init__(self, player, description="There isn't anything more to do in this room.", complete=False):
        self.player = player
        self.description = description
        self.complete = complete

    def start(self, last_command):
        self.complete = False

    def finish(self, last_command):
        self.complete = True
        self.player.objective = None


class EatBurger(Objective):
    def start(self, last_command):
        if self.player.room.name is 'kitchen':
            burger_here = False
            for i in self.player.room.inventory:
                if i.name == "burger":
                    burger_here = True
            if not burger_here:
                burger = Item("burger", 2, self.player, edible= True, accessible=False)
                self.player.room.inventory.append(burger)
                for i in self.player.room.inventory:
                    if i.name is "chair":
                        i.access_to.append(burger)

    def finish(self, last_command):
        if self.player.room.name is "kitchen":
            if last_command[0].lower() == 'eat' and \
                    last_command[1].lower() == 'burger' and not check_for_item("burger", self.player.room.inventory):
                print("Mmm, that was nice. What next?")
                self.complete = True
                self.player.objective = None
                self.player.room.objective_list = self.player.room.objective_list[1:]


class LookObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if last_command[0].lower() == 'look' and self.player.objective is not None:
            if self.player.room.objective_list:
                self.player.objective = self.player.room.objective_list[0]
                self.player.objective.start(last_command)
                print(self.player.objective.description)


class ScarePigeon(Objective):
    def start(self, last_command):
        pigeon = Entity("pigeon", self.player, skittish=True)
        self.player.room.inventory.append(pigeon)

    def finish(self, last_command):
        if self.player.room.name is "garden":
            if check_for_item("pigeon", self.player.room.inventory):
                return 0
            self.complete = True
            self.player.objective = None
            self.player.room.objective_list = self.player.room.objective_list[1:]
            print("The food is safe! Good job me.")


class SpillObjective(Objective):
    def start(self, last_command):
        juice = Item("juice", 0, self.player, accessible=False, edible=True)
        self.player.room.inventory.append(juice)

    def finish(self, last_command):
        if self.player.room.name is "kitchen":
            juice_here = False
            for i in self.player.room.inventory:
                if i.name is "juice":
                    juice_here = True
            if not juice_here:
                print("Nice and tidy.")
                self.complete = True
                self.player.objective = None
                self.player.room.objective_list = self.player.room.objective_list[1:]


class TeddyObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if self.player.room.name is "playroom" and check_for_item("teddy", self.player.room.inventory):
            print("Yay! Found the teddy.")
            self.complete = True
            self.player.objective = None
            self.player.room.objective_list = self.player.room.objective_list[1:]
