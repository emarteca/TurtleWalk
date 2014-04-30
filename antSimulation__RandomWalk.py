from turtle import Turtle
import random
import math

# Simple program to simulate an ant colony tracking food (very VERY simple...
# not really very biologically accurate).
# The user enters the (x, y) coordinates of the food locations, and the number
# of steps for the simulation.  Then, the ants start at position (0, 0) (centre
# of the screen) and walk around until they encounter (to a distance of 25) one
# of the specified food sources.
# When this occurs, the ant returns to the nest (i.e. (0, 0)) and another ant, in
# a different colour, starts out.


# function to run the ant simulation
# t --> the turtle
# x and y --> the x and y coordinates of the ant hill respectively
# rep --> number of steps for the simulation
# points --> the set of (x, y) coordinates for the food
def antTrack(t, x, y, rep, points):
    dist = 50 # length of an ant-step
    t.up()
    t.goto(x, y)
    t.down()
    degrees = t.heading()
    for index in range(rep): # run the simulation for the specified number of steps
        run = True
        while  run: # find a valid point to go to (cannot be outside the window)
            degrees = random.randint(0, 360)
            t.setheading(degrees)
            # x-y components of a distance of 50 along the new angle chosen
            w = dist * math.sin(degrees * 180 / math.pi) 
            z = dist * math.cos(degrees * 180 / math.pi) 
            if abs(x + w) < t.screen.window_width() / 2 and abs(y + z) < t.screen.window_height() / 2: # if the point is valid, update position
                 x += w
                 y += z
                 t.goto(x, y)
                 run = False
        for (a, b) in points:
            if abs(x - a) < 25 and abs(y - b) < 25: # if the new point is close (within 25) of one of the food locations
                t.up()
                t.home() # go back to the hill
                t.pencolor(random.random(), random.random(), random.random()) # pick a new colour
                t.down()
                


# main function controls user inputs and runs the program
def main():
        t = Turtle()
        # prompt user for all inputs
        iterations = input("Number of steps: ")
        print '--------------------------------------'
        print 'Enter the food coordinates - (0, 0) to exit'
        print '--------------------------------------'
        t.pencolor("red")
        t.screen.bgcolor("black")
        x = input("x-coordinate: ")
        y = input("y-coordinate: ")
        coords = [(x, y)]
        while x != 0 or y != 0:
            print '--------------------------------------'
            x = input("x-coordinate: ")
            y = input("y-coordinate: ")
            coords = [(x, y)]

        # run the simulation with the parameters specified
        antTrack(t, 0, 0, iterations, coords)
        t.hideturtle()

        print '\n\nProgram Done!'
        

main()
	

    
