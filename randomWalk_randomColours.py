from turtle import Turtle
import random
import math

# The random walk, with slightly different implementation.
# Instead of choosing a random point within range, this walk chooses a random
# angle and draws a line 80 units in this direction, from the previous point,
# if it is a valid point (i.e. within the window constraints).
# This is a random walk of fixed distance.
# This random walk is also not self-avoiding yet.
# And, the walk changes to a different random colour for every step.

# function to run the random walk (with random colours)
# t --> the turtle
# x and y --> the x and y coordinates of the starting position respectively
# rep --> number of steps for the walk
def randomWalkRandomColours(t, x, y, rep):
    dist = 80 # every step has a length of 80 (fixed distance)
    t.up()
    t.goto(x, y)
    t.down()
    degrees = t.heading()
    for index in range(rep): # run the walk for the specified number of steps
        while True :
            degrees = random.randint(0, 360)
            t.setheading(degrees)
            # choose a random position
            w = dist * math.sin(degrees * 180 / math.pi) 
            z = dist * math.cos(degrees * 180 / math.pi) 
            if abs(x + w) < t.screen.window_width() / 2 and abs(y + z) < t.screen.window_height() / 2:
                # if it's within the range, move to this position
                 x += w
                 y += z
                 # with a line of random colour
                 t.pencolor(random.random(), random.random(), random.random())
                 t.goto(x, y)
                 break

                
# main function controls user inputs and runs the program
def main():
        t = Turtle()
        # prompt the user for the number of steps
        iterations = input("Enter the number of reps: ")
        t.pencolor("red")
        t.screen.bgcolor("blue")
        t.width(10)

        # run the walk with the parameters specified
        # this walk starts at the origin (centre of the window) every time
        randomWalkRandomColours(t, 0, 0, iterations)
        t.hideturtle()

        print '\n\nProgram Done!'
        

main()
	

    
