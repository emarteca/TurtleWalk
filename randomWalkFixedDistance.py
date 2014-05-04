from turtle import Turtle
import random
import math

# The random walk, with slightly different implementation.
# Instead of choosing a random point within range, this walk chooses a random
# angle and draws a line 80 units in this direction, from the previous point,
# if it is a valid point (i.e. within the window constraints).
# This is a random walk of fixed distance.
# This random walk is also not self-avoiding yet.
# It's the same as the randomWalkRandomColours, but with a constant colour (red).

# function to run the random walk (with random colours)
# t --> the turtle
# x and y --> the x and y coordinates of the starting position respectively
# rep --> number of steps for the walk
def randomWalkFixedDistance(t, x, y, rep):
    dist = 80 # every step has a length of 80 (fixed distance)
    t.up()
    t.goto(x, y)
    t.down()
    degrees = t.heading()
    check = 0
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
                 t.goto(x, y)
                 break
        check += 1
            
    print check
                
# main function controls user inputs and runs the program
def main():
        t = Turtle()
        # prompt user for all inputs
        x = input("Enter the x-coordinate of the starting point: ")
        y = input("Enter the y-coordinare of the starting point: ")
        iterations = input("Enter the number of reps: ")
        t.pencolor("red")
        t.screen.bgcolor("black")

        # run the walk with the parameters specified
        randomWalkFixedDistance(t, x, y, iterations)
        t.hideturtle()

        print '\n\nProgram Done!'
        

main()
	

    
