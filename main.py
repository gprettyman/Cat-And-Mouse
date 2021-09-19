#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
import random

# This program requires LEGO EV3 MicroPython v2.0 or higher.


# Create objects
mouseRobot = EV3Brick()
mouseRobot.speaker.set_speech_options(language = 'fr-fr', voice = None, speed = None, pitch = None)  # Sets robot to use French for text-to-speech
eyes = ColorSensor(Port.S3)
leftMotor = Motor(Port.B, positive_direction = Direction.COUNTERCLOCKWISE, gears = None)
rightMotor = Motor(Port.C, positive_direction = Direction.COUNTERCLOCKWISE, gears = None)

wheelDiameter = 30  #Edit as needed. Diameter of wheels in millimeters (mm)
axleTrack = 120     #Edit as needed. Distance between wheels in millimeters (mm)

wheels = DriveBase(leftMotor, rightMotor, wheelDiameter, axleTrack)     # Sets up DriveBase, allows controlling both motors at same time (easier for driving motion)
quitProgram = False
currentX = 0
currentY = 0
currentOrientation = 1  # 1 = North, 2 = East, 3 = South, 4 = West
newOrientation = random.randint(1,4)        # Creates a random direction to move in
randomMove = random.randint(1,5)            # Creates a random distance to move

# Makes the robot return back to its starting position
def runHome():
    global currentOrientation       # Declaring variables as global in each method allows them to be used/changed everywhere
    global newOrientation
    global currentX
    global currentY
    newOrientation = 3          # Sets the direction to South (ie. towards y=0), then moves that direction
    reorientDirection()
    while currentY != 0:
        wheels.straight(10)
        currentY -= 1
    newOrientation =  4         # Sets the direction to West (ie. towards x=0), then moves that direction
    reorientDirection()
    while currentX != 0:
        wheels.straight(10)
        currentX -= 1
    newOrientation = 1          # Sets the direction back to North so robot is "reset" to original position
    reorientDirection()


# Turns the robot to face the new direction
def reorientDirection():
    global currentOrientation
    global newOrientation
    while currentOrientation != newOrientation:         # Turns the robot until it is facing the new direction
        if currentOrientation < newOrientation:         # Lines 55-60 turn the robot the direction closest to the new direction
            wheels.turn(90)
            currentOrientation += 1
        elif currentOrientation > newOrientation:
            wheels.turn(-90)
            currentOrientation -= 1


# Checks the robot's position to see if it is hitting a "wall"
# Returns True if hitting a "wall," False if not
def directionWall():
    global currentOrientation
    global currentX
    global currentY
    if currentOrientation == 1:     # Checks if the robot is facing North, then if it is the final spot before the wall (y=49), etc.
        if currentY == 49:
            return True
        else:
            return False
    elif currentOrientation == 2:
        if currentX == 49:
            return True
        else:
            return False
    elif currentOrientation == 3:
        if currentY == 0:
            return True
        else:
            return False
    elif currentOrientation == 4:
        if currentX == 0:
            return True
        else:
            return False


# Keeps track of the robot's position (x, y coordinates) from (0,0) to (49,49)
def logPosition():
    global currentOrientation
    global currentX
    global currentY
    if currentOrientation == 1:             # If robot is facing North, then each time it moves, it will move one "space" on the y-axis, etc.
        currentY += 1                       # Updates the currentY or currentX variables so it knows where it is
    elif currentOrientation == 2:
        currentX += 1
    elif currentOrientation == 3:
        currentY -= 1
    elif currentOrientation == 4:
        currentX -= 1


#Main Program: Runs around randomly until finding "the cat," then returns home and quits program
mouseRobot.speaker.say("Quand le chat n'est pas là les souris dansent")     # Says the phrase before moving
while quitProgram != True:
    if eyes.color() == Color.YELLOW:  # Checks for the "cat" (Can change the color here)
        mouseRobot.speaker.say("Oh non le chat est revenu")
        runHome()               # Runs away if it sees the "cat"
        quitProgram = True      # Sets this variable to True so it will quit after running home
    elif randomMove == 0:                       #If it has moved the random distance chosen
        mouseRobot.speaker.say("Quand le chat n'est pas là les souris dansent")     # Says the phrase again
        newOrientation = random.randint(1,4)   # Picks a new random direction
        reorientDirection()                    # Faces the new direction
        randomMove = random.randint(1,5)       # Picks a new random distance to move
    elif randomMove != 0:                       # If it has not yet moved the random distance chosen:
        if directionWall() == True:                 # Checks to ensure it is not "hitting a wall"
            randomMove = 0                              # If it is "hitting a wall", sets the movement to 0 so it will not move forward this time
        else:
            wheels.straight(10)                         # If it is not "hitting a wall," moves 1cm (10mm) forward, "one space" in the coordinate grid
            logPosition()                                   # Logs this movement to the currentX or currentY variable, depending on which way it is facing
