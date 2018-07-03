from Setup import setup
from Restart import RestartAction
from Intro import intro
from Objectives import LookObjective

# intro to create player
responses = intro()

myPlayer = setup(responses[0].capitalize(), responses[1])
restart = RestartAction("restart", myPlayer)
myPlayer.action_list.append(restart)

# main play
while True:
    myActionText = input(">")
    myActionText = myActionText.split()
    if len(myActionText) == 1:
        myPlayer.execute_action(myActionText[0])
    if len(myActionText) == 2:
        myPlayer.execute_action(myActionText[0], myActionText[1])
    if len(myActionText) > 2:
        myPlayer.execute_action(myActionText[0], myActionText[1], myActionText[2])
    myPlayer.objective.finish(last_command=myActionText)
    if myPlayer.objective is None:
        myPlayer.objective = LookObjective(myPlayer)
