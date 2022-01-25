### Adventure game project ###
### By Charles Mogayzel
### 01/24/2022

import time
import random

def pause_print(printMessage):
    print(printMessage)
    time.sleep(2)


def intro(item, option):
    pause_print("You find your self in the forest in the middle of winter")
    pause_print("You see a cabin in the distances but not sure if someone is home or not.")
    pause_print("You are a " + option + " .")
    

def forest(item, option):
    pause_print("You are approaching the door of the cabin.\n")
    pause_print("What do you do.")
    house(item,option)
    


def  house(item,option):
    pause_print("Enter 1 to enter cabin.")
    pause_print("Enter 2 to peer into cabin.")
    pause_print("What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == "1":
            break
        elif choice == "2":
            break
        else:
            pause_print("Error, you did choose 1 or 2")
            play_again()
            break

def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y" or again == "Y":
        pause_print("\n\n\nExcellent! Restarting the game ...\n\n\n")
        pause_print()
    elif again == "n" or again == "N" :
        pause_print("\n\n\nThanks for playing!\n\n\n")
    else:
        play_again()


def gamePlay():
    item = []
    option = random.choice(["soldier","hunter","survivalist","park ranger"])
    intro(item,option)



gamePlay()
