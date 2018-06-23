from action import Action


class GoAction(Action):
    def execute(self, item = None):
        if item is None:
            print("Where should I go?")
            return 0
        for r in self.player.room.connections:
            if item.lower() == r.name.lower():
                if not self.player.on_furniture:
                    self.player.room = r
                    self.player.room.player_present = False
                    r.player_present = True
                    return 0
                print("I'm on a {0}! I need to get off.".format(self.player.on_furniture.name))
        print("I can't go there.")
