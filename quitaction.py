from action import Action


class QuitAction(Action):
    def execute(self, item=None):
        exit(0)

