from Items import *
from HelperFunctions import *
from Entity import Entity
from Room import Room


class Objective:
    def __init__(self, player, description="There isn't anything more to do in this room.",
                 complete=False, prerequisites=[]):
        self.player = player
        self.description = description
        self.complete = complete
        self.prerequisites = prerequisites

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
                self.player.completed_objectives.append("EatBurger")


class LookObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if len(self.player.completed_objectives) == 5:
            print("Congratulations {0}! You've completed all the objectives. Feel free to ".format(self.player.name),
                  "continue running about.")
        if last_command[0].lower() == "look" and self.player.objective is not None:
            for objective in self.player.room.objective_list:
                prerequisites_met = True
                for requirement in objective.prerequisites:
                    if requirement not in self.player.completed_objectives:
                        prerequisites_met = False
                if prerequisites_met and not objective.complete:
                    self.player.objective = objective
                    self.player.objective.start(last_command)
                    print(self.player.objective.description)
                    return


        #if last_command[0].lower() == 'look' and self.player.objective is not None:
        #    for objective in self.player.room.objective_list:
        #        if not objective.complete:
        #            for requirement in objective.prerequisites:
        #                if requirement not in self.player.completed_objectives:
        #                    break
        #                self.player.objective = objective
        #                self.player.objective.start(last_command)
        #                print(self.player.objective.description)
        #                return


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
            print("The food is safe! Good job me.")
            self.player.completed_objectives.append("ScarePigeon")


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
                self.player.completed_objectives.append("SpillObjective")


class TeddyObjective(Objective):
    def start(self, last_command):
        pass

    def finish(self, last_command):
        if self.player.room.name is "playroom" and check_for_item("teddy", self.player.room.inventory):
            print("Yay! Found the teddy.")
            self.complete = True
            self.player.objective = None
            self.player.completed_objectives.append("TeddyObjective")


class OpenBasement(Objective):
    def start(self, last_command):
            trapdoor = LockableItem("trapdoor", 100, self.player, accessible=True)
            self.player.room.inventory.append(trapdoor)
            latchkey = KeyItem("latchkey", 1, self.player, access_to=[trapdoor])
            flowerpot = BreakableItem("flowerpot", 2, self.player, access_to=[latchkey])
            self.player.room.inventory.append(flowerpot)

        #if "SpillObjective" in self.player.completed_objectives:
        #    trapdoor = LockableItem("trapdoor", 100, self.player, accessible=True)
        #    self.player.room.inventory.append(trapdoor)
        #    latchkey = KeyItem("latchkey", 1, self.player, access_to=[trapdoor])
        #    flowerpot = BreakableItem("flowerpot", 2, self.player, access_to=[latchkey])
        #   self.player.room.inventory.append(flowerpot)
        #else:
        #    self.player.objective = None

    def finish(self, last_command):
        for item in self.player.room.inventory:
            try:
                if not item.locked and item.name == "trapdoor":
                    self.player.room.inventory.remove(item)
                    backpack = CarrierItem("backpack", 2, self.player, capacity=6)
                    basement = Room("basement", inventory=[backpack], connections=[self.player.room])
                    self.player.room.connections.append(basement)
                    trapdoor = StairsItem("trapdoor", 100, self.player, access_to=[basement])
                    self.player.room.inventory.append(trapdoor)
            except AttributeError:
                pass
        if self.player.room.name == "basement":
            print("I made it!")
            self.complete = True
            self.player.objective = None
            self.player.completed_objectives.append("OpenBasement")
