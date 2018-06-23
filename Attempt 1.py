from colorama import *
init(autoreset=True)
init(convert=True)

dogs = ["Beagle", "Collie", "Great Dane", "dumbass"]
dog_difficulty = ["easy", "medium", "hard", "non-existent"]
complete = 0

print("Hi, welcome to the dog text game! Choose your difficulty level: ")
while complete == 0:
    difficulty = input(Fore.GREEN + "Easy, Medium or Hard.\n")
    for ii in range(4):
        if difficulty.lower() == dog_difficulty[ii]:
            breed = dogs[ii]
            print("You have chosen {0} so you are a {1}.".format(difficulty.lower(), breed))
            complete = 1
            break
        if ii == 3:
            print("Oops, that wasn't one of the options. Please type one of these:")

name = input("What's your name?\n").title()
print("Nice to meet you {0} the {1}! ".format(name, breed))
print("Let's get straight to it, you're Sophie's new dog and "
      "it's your job to make sure everything goes smoothly at this party!\n"
      " You can get your bearings if you look around.")

commands = ["look", "go", "bark", "give", "pull"]
thing = ["pigeon", "ball", "woman", "lyric", "food"]
position_looks = ["There are a lot of people around and it's noisy.\n"
        "The table with food on it is in the middle of the room.\n"
            "The pigeon in the window seems to be eyeing the food, I should go scare off that pigeon.",
        "The pigeon is right there, I should definitely bark to get rid of it!",
        "There's a little girl over there that looks lonely. Let's cheer her up!",
        "There're a few balls here. I could give the girl a ball for fetch!",
        "There's a woman crying over there. Maybe I can help her.",
        "The woman keeps saying Lyric. I know where she is! Lets get her!",
        "Lyric hasn't noticed me or her mother. I'll have to pull the girl to her mother!",
        "Now what."
              ]


# scaring away a pigeon
complete = 0
position = 0
while complete == 0:
    type_input = input()
    if type_input.lower()[0:4] == commands[0]:
        print("{0}".format(position_looks[position]))
    if type_input.lower() == commands[1]:
        print("The pigeon is quite high up... Maybe if I bark that will scare it.")
        position = 1
    if type_input.lower() == commands[2] and position == 1:
        print("The pigeon has flew off! Yay! I should look around for anything else I'm needed for.")
        position = 2
        complete = 1
    if type_input not in commands[0:2]:
        print("What should I do?")


# cheering up lyric
complete = 0
while complete == 0:
    type_input = input()
    if type_input == commands[0]:
        print("{0}".format(position_looks[position]))
    if type_input == commands[1]:
        position = 3
        print("Here we are, now what can I do?")
    if type_input == "{0} {1}".format(commands[3], thing[1]):
        print("The girl isn't throwing the ball but I got pats and she seems happier. "
              "She says her name is Lyric! My job is done.")
        position = 4
        complete = 1


complete = 0
while complete == 0:
    type_input = input()
    if type_input.lower() == commands[0]:
        print("{0}".format(position_looks[position]))
    if type_input.lower() == commands[1]:
        position = 5
        print("{0}".format(position_looks[position]))
    if type_input.lower() == "{0} {1}".format(commands[1],thing[3]):
        position = 6
        print(position_looks[position])
    if type_input.lower() == "{0} {1}".format(commands[4],thing[3]):
        position = 7
        print("The woman seems happy now she's got Lyric. Another happy customer.")
        complete = 1
