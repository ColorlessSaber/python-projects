#
# Python: 3.13.4
#
# Author: Michael Heilman
#
# Purpose: The Tech Academy - Python Course. Creating our first program together.
#           Demonstrating how to pass variables from function to function while producing
#           a functional game.
#

def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player for
        playing again and continue with the game
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will ge greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approached you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = nice + 1
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = mean + 1
            stop = False
    score(nice,mean,name)

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    if nice > 2:    # if condition is valid, call win function
        win(nice,mean,name)
    elif mean > 2:    # if condition is valid, call lose function
        lose(nice,mean,name)
    else:   # else call nice_mean function
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nWay to go, {}! you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nGame over you big meany! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N)\n>>>: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        elif choice == "n":
            print("\nUntil next time! Later!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO'\n>>>: ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # name is not reset given the user choice to play again.
    start(nice, mean, name)


if __name__ == "__main__":
    start()
