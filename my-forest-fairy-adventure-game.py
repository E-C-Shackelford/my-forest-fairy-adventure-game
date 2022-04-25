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