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


def left_path():
    print_pause("You travel down the left path\n"
                "and encounter a scary, evil " + villan + ".")
    print_pause("The " + villan + " is searching for the magical stone\n"
                "in your sachel.", 3)
    print_pause("The " + villan + " asks if you've seen any of the\n"
                "forest fairies' magical stones.", 4)
    print_pause("You feel a moment of panic because the stone in your sachel\n"
                "might very well be one of those stones.", 3)
    print_pause("The " + villan + " lunges towards you.")
    print_pause("Will you run away from or fight the evil " + villan + "\n"
                "so he can't get into your sachel\n"
                "and take the stone?")
    print_pause("Please enter the action you'd like to take:")
    action = valid_input("1. run\n"
                         "2. fight\n", ["1", "2"])
    if action == '1':
        print_pause("You run away as fast as you can!")
        print_pause("You make it back to the start of the path and\n"
                    "encounter another " + villan + "!", 3)
        print_pause("You try fighting off the second " + villan + " but then\n"
                    "the other " + villan + " approaches you.", 3)
        print_pause("They take your sachel and find the stone inside!")
        print_pause("The " + villan + " now has the magical stone.")
        print_pause("I'm sorry, you lost the game.")

    elif action == '2':
        print_pause("A walking-stick is attached to your sachel,\n"
                    "so you quickly grab it,\n"
                    "to fight off the " + villan + ".", 3)
        print_pause("The " + villan + " is stronger than you thought\n"
                    "and is getting angrier.")
        print_pause("You call for help.")
        print_pause("The forest fairies hear your call\n"
                    "and come to the rescue.", 3)
        print_pause("They shine their bright light onto the " + villan + ".")
        print_pause("Their bright light transmutes the " + villan + "'s\n"
                    "anger and aggression\n"
                    "into a calm stillness.", 4)
        print_pause("The " + villan + " then leaves,\n"
                    "and retreats down the hill,\n"
                    "to his cave.")
        print_pause("You are all safe now.\n"
                    "You thank the fairies for their heroism and\n"
                    "reveal the stone you found.", 4)
        print_pause("The fairies thank you for returning their stone and\n"
                    "invite you to their forest festival.", 3)
        print_pause("Will you attend the fairies' forest festival?\n"
                    "Please select whether or not you'll attend:")
        attend = input("1. yes\n"
                       "2. no\n")
        if attend == '1':
            print_pause("You attend their magical forest festival.")
            print_pause("You learn about the healing properties of\n"
                        "plants and stones!")
            print_pause("Congrats, you won the game!")

        elif attend == '2':
            print_pause("The fairies go off to their festival\n"
                        "and you return home.")
            print_pause("Even though you're missing the forest festival,\n"
                        "you returned the fairies' stone,\n"
                        "so you won the game!")

        else:
            print_pause("Please select whether or not you'll attend:")
            attend = input("1. yes\n"
                           "2. no\n")
            if attend == '1':
                print_pause("You attend their magical forest festival.")
                print_pause("The forest fairies teach you about\n"
                            "the healing properties of plants and stones!", 3)
                print_pause("Congrats! You won the game!")
            elif attend == '2':
                print_pause("Even though you're missing the forest festival,\n"
                            "you returned the stone to the forest fairies\n"
                            "and so you still won the game!")


def right_path():
    print_pause("As you travel down the right path,\n"
                "you encounter magical fairies\n"
                "who love and celebrate stones.")
    print_pause("They've lost one of their stones,\n"
                "so you show them the stone you found.")
    print_pause("The fairies are overjoyed!", 3)
    print_pause("Because you found their stone\n"
                "and returned it,\n"
                "the fairies want to teach you about its healing properties\n"
                "and want you to keep the stone as a gift!")
    print_pause("You saved the day and are now\n"
                "a trusted friend of the forest fairies!")
    print_pause("Congrats, you won the game!")