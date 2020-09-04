def intro():
    dogs = [["beagle", "b"], ["collie", "c"], ["great dane", "gd"], ["mutt", "m"], ["skip","s"]]
    yeses = ["y", "yes", 1]
    noes = ["n", "no", 0]

    print("Hi, welcome to the dog text game! What type of dog would you like to be: ")
    breed_chosen = False
    breed_choice = 2
    while not breed_chosen:
        choice = input("A beagle, a collie or a great dane?\n")
        for ii in range(5):
            if choice.lower() in dogs[ii]:
                print("You have chosen {0}.".format(dogs[ii][0]))
                breed_choice = dogs[ii][0]
                breed_chosen = True
                break
            if ii is 4:
                print("Oops, that wasn't one of the options. Please type one of these:")

    if breed_choice == "skip":
        return ["Me", "mutt"]

    name_chosen = False
    name_choice = "Player"
    while not name_chosen:
        name_choice = input("Now what's your name?\n")
        answer = input("Is {0} correct?\n".format(name_choice.capitalize()))
        if answer.lower() in yeses:
            name_chosen = True
            print("Great! You're in the garden. "
                  "Look around to get started and type help to find out what you can do. Good luck!")

    return [name_choice, breed_choice]