class Item:
    def __init__(self, name, weight, player, edible=False, accessible=True, access_to=[]):
        self.name = name
        self.weight = weight
        self.player = player
        self.edible = edible
        self.accessible = accessible
        self.access_to = access_to

    def use_item(self, second_item=None):
        print("This item can't be used.")
