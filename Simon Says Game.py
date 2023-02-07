#Add Phidgets Library | You used Python's package manager to install the Phidget libraries on your computer. The import statements below give your program access to that code.
from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.DigitalOutput import *
#Required for sleep statement 
import time
from random import *
 
#Create | Create objects for your buttons and LEDs.
redButton = DigitalInput()
redLED =  DigitalOutput()
greenButton = DigitalInput()
greenLED = DigitalOutput()
 
#Address | Address your four objects which lets your program know where to find them.
redButton.setHubPort(0)
redButton.setIsHubPortDevice(True)
redLED.setHubPort(1)
redLED.setIsHubPortDevice(True)
greenButton.setHubPort(5)
greenButton.setIsHubPortDevice(True)
greenLED.setHubPort(4)
greenLED.setIsHubPortDevice(True)

#Open | Connect your program to your physical devices.
redButton.openWaitForAttachment(1000)
redLED.openWaitForAttachment(1000)
greenButton.openWaitForAttachment(1000)
greenLED.openWaitForAttachment(1000)
        
#Use your Phidgets | This code will turn on the LED when the matching button is pressed and turns off the LED when the matching button is released. The sleep function slows down the loop so the button state is only checked every 150ms.

def Randomize(x):
    l = []
    i = 0
    for i in range(0,x):
        C = randint(0,1)
        if C == 0:
            greenLED.setState(True)
            redLED.setState(False)
            l.append(0)
        else:
            greenLED.setState(False)
            redLED.setState(True)
            l.append(1)
        time.sleep(0.5)
        print(l)
        greenLED.setState(False)
        redLED.setState(False)
        time.sleep(0.5)
    return l

def player1(x):
    l = []
    i = 0
    while i < x:
        if greenButton.getState():
            greenLED.setState(True)
            l.append(0)
            i += 1
            print(l)
        elif redButton.getState():
            redLED.setState(True)
            l.append(1)
            i += 1
            print(l)
        time.sleep(0.5)
        greenLED.setState(False)
        redLED.setState(False)
        time.sleep(0.5)
    return l
 
def player2(l):
    for i in range(0, len(l)):
        if l[i] == 0:
            greenLED.setState(True)
            time.sleep(0.5)
            greenLED.setState(False)
            time.sleep(0.5)
        else:
            redLED.setState(True)
            time.sleep(0.5)
            redLED.setState(False)
            time.sleep(0.5)
            
def answers(x, l):
    status = True
    i = 0
    while not redButton.getState() and not greenButton.getState():
        while i < x:
            time.sleep(0.5)
            if redButton.getState():
                redLED.setState(True)
                time.sleep(0.5)
                redLED.setState(False)
                c = 1
                if c != l[i]:
                    print("You Lost!")
                    status = False
                i += 1
            elif greenButton.getState():
                greenLED.setState(True)
                time.sleep(0.5)
                greenLED.setState(False)
                c = 0
                if c != l[i]:
                    print("You Lost!")
                    status = False
                i += 1
        if status == True:
            print("You Won!")
            break
print("Choose Red for single player and Green for multiplayer")
print(" ")
while True:
    if redButton.getState():
        print("Single player Mod")
        print(" ")
        difficulty = int(input("Choose a difficulty From 1-5 : ")) *2
        if difficulty > 10:
            difficulty = 10
        l = Randomize(difficulty)
        answers(difficulty,l)
        break
    elif greenButton.getState():
        print("Multi player Mod")
        print(" ")
        difficulty2 = int(input("Choose a difficulty From 1-5 : ")) *2
        if difficulty2 > 10:
            difficulty2 = 10
            print("Difficulty Set to 2")
        print(f'One player should choose a pattern of colors for the other player to follow, After the green and red LEDs go off insert {difficulty2} patterns ')
        for i in range(0,5):
            redLED.setState(True)
            greenLED.setState(True)
            time.sleep(0.1)
            redLED.setState(False)
            greenLED.setState(False)
        l = player1(difficulty2)
        print("player 2 may now follow the LED and once over will play")
        time.sleep(2)
        player2(l)
        answers(difficulty2,l)
        break
    time.sleep(0.15)
    
  
