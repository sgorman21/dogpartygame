class Entity:
    def __init__(self, name, player, skittish=False, accessible=True):
        self.name = name
        self.player = player
        self.skittish = skittish
        self.accessible = accessible

    def speech(self):
        print("I don't have anything to say")