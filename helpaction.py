from action import Action


class HelpAction(Action):
    def execute(self, item=None):
        actions = "{0}".format(self.player.action_list[0].name.lower())
        for i in range(1,len(self.player.action_list)-1):
            actions += ", {0}".format(self.player.action_list[i].name.lower())
        actions += " and {0}.".format(self.player.action_list[len(self.player.action_list)-1].name.lower())
        print("The possible actions are {0}".format(actions))
