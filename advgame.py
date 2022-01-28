#Adventure game project
#By Charles Mogayzel
#01/24/2022


from email import message
import time
import random

def pause_print(printMessage,delay=0):
    print(printMessage)
    
def intro(item, option):
    message = ("You are walking through the forsest and come up on a old cabin.\n"
    "You notice the cabin is very old and looks abandond."
    "You are very cold and hungry and the cabin would provide shelter from the cold "
    "and could have food and firewood to stay warm, but your guts tell you there is something wrong.\n"
    "What do you do?"
    "You are a " + option + " .\n"
    )
    pause_print(message,2)

def zombieSuprise():
         message = ("You enter the cabin and are surpised by a zombie.\n"
         "You are killed by the zombie." "The end.\n" )
         pause_print(message,2)

def zombieAttack(randomItem,option): 
       pause_print("You enter the cabin with your " + randomItem + " and attack the zombie.",2)
       if randomItem == "stick" :
           pause_print("You are killed by the zombie " + randomItem + " was not enough to defeat the zombie.",2)
           pause_print("The end")
       elif randomItem == "axe" :
            pause_print("Your " + randomItem + " defeats the zombine and you have enough food and firewood to survive winter.")
            
def walkaround(randomItem,option) :
    message = ("You walk around the cabin to find there is a zombie in the cabin."
    "what do you do?\n" "Enter 1 to enter cabin.\n"
    "Enter 2 walk away and find another cabin.")
    pause_print(message,2)
    choice = input("Enter 1 or 2 ")
    while True :
          if choice == "1":
              zombieAttack(randomItem, option)
              break
          elif choice == "2":
            message = ("You chose to move on and find another cabin that doesn't a zombie in it.\n"
            "Your choice causes you to freeze and not find another cabin.\n"
            "The end.\n")
            pause_print(message,2)
            break
          else:
             pause_print("Error, you did choose 1 or 2. ",2)

def cabin(randomItem,option):
    message = ("Enter 1 to enter cabin.\n" "Enter 2 to peer into cabin.\n" "What would you like to do?\n")
    pause_print(message,1)
    while True:
        choice = input("(Please enter 1 or 2 ): ")
        if choice == "1":
            zombieSuprise()
            play_again()
            break
        elif choice == "2":
            walkaround(randomItem,option)
            play_again()
            break
        else:
            pause_print("Error, you did choose 1 or 2. ",2)
           
def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y" or again == "Y":
        pause_print("\n\n\nExcellent! Restarting the game ...\n\n\n")
        gamePlay()
    elif again == "n" or again == "N" :
        pause_print("\n\n\nThanks for playing!\n\n\n")
    else:
        play_again()

def  gamePlay():
    randomItem = random.choice(["stick" ,"axe"])
    option = random.choice(["soldier" , "hunter" , "survivalist" , "park ranger"])
    intro(randomItem, option)
    cabin(randomItem, option)

gamePlay()
