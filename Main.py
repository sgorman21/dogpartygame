from setup import setup
from restartaction import RestartAction


# intro to create player
dogs = ["beagle", "collie", "great dane", "mutt"]
yeses = ["y", "yes", 1]
noes = ["n", "no", 0]

print("Hi, welcome to the dog text game! What type of dog would you like to be: ")
breed_chosen = False
breed_choice = 2
while not breed_chosen:
    choice = input("Beagle, collie or great dane?\n")
    for ii in range(4):
        if choice.lower() == dogs[ii]:
            breed_choice = ii
            print("You have chosen {0}.".format(dogs[ii]))
            breed_chosen = True
            break
        if ii is 3:
            print("Oops, that wasn't one of the options. Please type one of these:")

name_chosen = False
while not name_chosen:
    name_choice = input("Now what's your name?\n")
    answer = input("Is {0} correct?\n".format(name_choice.capitalize()))
    if answer in yeses:
        name_chosen = True

myPlayer = setup(name_choice.capitalize(), dogs[breed_choice])
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
        myPlayer.execute_action((myActionText[0], myActionText[1], myActionText[2]))
