### Adventure game project ###
### By Charles Mogayzel
### 01/24/2022

import time
import random

def pause_print(printMessage):
    print(printMessage)
    time.sleep(2)


def intro(item, option):
    pause_print("You find your self in the middle of a desert, it is hot and no shade or water")
    pause_print("You see something in the distant, but don't know if it is real or not.")
    pause_print("You are a " + option + " .")
    

def mirage(option2):
    if (option2):
        pause_print("You find a small body of water to quench your thirst")
        pause_print("You get a drink of water and continue walking past the cave")
    else:
        pause_print("Afer for walking for hours or days you learn it was just a marage and there is no water.")
        pause_print("You continue walking and find a cave")


def gamePlay():
    item = []
    option = random.choice(["soldier","merchent","wanderer","camel"])
    intro(item,option)



gamePlay()
