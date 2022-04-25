import time
import random

def print_pause(message, pause=2):
    print(message)
    time.sleep(pause)


def random_villan():
    villan_choice = ["troll", "werewolf", "goblin", "orc"]
    villan = random.choice(villan_choice)


def intro():
    print_pause("You're in a magical forest, walking along a forest stream.")
    print_pause("As you walk along the stream,\n"
                "you find a beautiful blue stone.")
    print_pause("You pick up the stone to look at it more closely.", 3)
    print_pause("The stone is mesmerizing.")
    print_pause("Little do you know,\n"
                "it has very powerful properties.", 3)
    print_pause("You approach a fork in the road.")
    print_pause("You can either take the path to your left,\n"
                "or that to your right.", 3)
    print_pause("You place the stone in your sachel\n"
                "and look at each path.")


def valid_input(prompt, options):
    response = input(prompt)
    if response not in options:
        print_pause("Invalid input, please try again")
        return valid_input(prompt, options)
    return response


def path_choice():
    print_pause("Which path will you take?\n"
                "Please enter the path you would like to take:")
    path = valid_input("1. left path\n"
                       "2. right path\n", ["1", "2"])
    if path == '1':
        left_path()
    elif path == '2':
        right_path()