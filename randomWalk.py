from turtle import Turtle
import random

# The original random walk code!  Not self-avoiding yet.
# The method behind this is different than that of the ant simulation and the
# self-avoiding walks developed later -
# it chooses random x and y coordinates within the bounds of the window (/2), and
# moves to this point.  So, it is a random walk with random distance.

# function to run the random walk
# t --> the turtle
# x and y --> the x and y coordinates of the ant hill respectively
# rep --> number of steps for the walk 
def randomWalk(t, x, y, rep):
    t.up()
    t.goto(x, y)
    t.down()
    for index in range(rep): # run the walk for the specified number of steps
        # choose a random position, within range, to move to
        x = random.randint(-(t.screen.window_width() / 2) , t.screen.window_width() / 2)
        y = random.randint(-(t.screen.window_height() / 2), t.screen.window_height()/ 2)
        t.goto(x, y)
    t.hideturtle()

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
        randomWalk(t, x, y, iterations)

        print '\n\nProgram Done!'
        

main()
	

    
