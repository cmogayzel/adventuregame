### Adventure game project ###
### By Charles Mogayzel
### 01/24/2022

import time
import random

def pause_print(printMessage):
    print(printMessage)
    time.sleep(2)


def intro(item, option):
    pause_print("You are walking through the forsest and come up on a old cabin.\n")
    pause_print("You notice the cabin is very old and looks abandond.")
    pause_print("You are very cold and hungry and the cabin would provide shelter from the cold ")
    pause_print("and could have food and firewood to stay warm, but your guts tell you there is something wrong.")
    pause_print("What do you do?")
    pause_print("You are a " + option + " .")

def zombieSuprise():
         pause_print("You enter the cabin and are surpised by a zombie.")
         pause_print("You are killed by the zombie.")
         pause_print("The end")
       

def zombieAttack(randomItem,options): 
       pause_print("You enter the cabin with your " + randomItem + " and attack the zombie.")
       if randomItem == "stick":
           pause_print("You are killed by the zombie " + randomItem + " was not enough to defeat the zombie.")
           pause_print("The end")
       elif randomItem == "axe":
            pause_print("Your " + randomItem + " defeats the zombine and you have enough food and firewood to survive winter.")
            

def walkaround():
     pause_print("You walk around the cabin to find there is a zombie in the cabin.")
     pause_print("what do you do?")
     pause_print("Enter 1 to enter cabin.")
     pause_print("Enter 2 walk away and find another cabin.")
     choice = input("Enter 1 or 2 ")
     if choice == "1":
         zombieAttack()
     elif choice == "2":
         pause_print("You chose to move on and find another cabin that doesn't a zombie in it.")
         pause_print("Your choice causes you to freeze and not find another cabin.")
         pause_print("The end.")



def cabin(randomItem,option):
    pause_print("Enter 1 to enter cabin.")
    pause_print("Enter 2 to peer into cabin.")
    pause_print("What would you like to do? ")
    while True:
        choice = input("(Please enter 1 or 2 )")
        if choice == "1":
            zombieSuprise()
            play_again()
            break
        elif choice == "2":
            walkaround()
            play_again()
            break
        else:
            pause_print("Error, you did choose 1 or 2. ")
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
    randomItem = random.choice(["stick","axe"])
    option = random.choice(["soldier","hunter","survivalist","park ranger"])
    intro(randomItem,option)
    cabin(randomItem,option)


gamePlay()
