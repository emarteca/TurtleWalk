from turtle import Turtle
import random
import math
import interceptInRange

# The self-avoiding walk!!  Yay!
# This self-avoiding walk (fixed distance) is much faster than the previous implementation!
# This is because the approach is no longer angle-based.  The turtle.setHeading(...) is what
# was slowing it down.
#
# This is a fixed-distance walk, where the user is prompted for the step length.
# The functionality is as follows:
#       - draw 2 lines (i.e. 3 points)
#       - keep track of all the points in the walk
#       - keep track of the equations of the lines between all adjacent points
#       - for the rest of the steps, before walking to a new point, ensure that
#         the step between the last point and the new point does not intersect
#         any of the previous steps
# If the walk gets stuck for 100 tries (i.e. checking 100 points) then it exits.

# function to run the self-avoiding walk
# t --> the turtle
# x and y --> the x and y coordinates of the starting position respectively
# rep --> number of steps for the walk (unless it gets stuck)
# dist --> length of the step
def selfAvoidingWalk(t, x, y, rep, dist):
    # first 3 points can't cross
    
    t.up()
    t.goto(x, y)
    t.down()
    arrayOfPoints = [(x, y)] # list of points in the walk
    
    step = random.random() * dist * ((-1) ** (random.randint(1, 2)))
    y += math.sqrt(dist**2 - step**2) * ((-1)**(random.randint(1, 2)))
    x += step
    arrayOfPoints += [(x, y)]
    t.goto(x, y)
    (m, b) = solveLinearEquation(arrayOfPoints[0], arrayOfPoints[1]) # list of linear equations (in form (slope, y-intercept)) for all adjacent pairs of points in the walk
    linearEquations = [(m, b)]
    
    step = random.random() * dist * ((-1) ** (random.randint(1, 2)))
    y += math.sqrt(dist**2 - step**2) * ((-1)**(random.randint(1, 2)))
    x += step
    arrayOfPoints += [(x, y)]
    t.goto(x, y)
    (m, b) = solveLinearEquation(arrayOfPoints[1], arrayOfPoints[2])
    linearEquations += [(m, b)]
    
    # here, 3 points exist and 2 lines have been drawn.
    # len(arrayOfPoints) == 3 and 2 iterations have been done

    for index in range(rep - 2): # index == 0 when len(arrayOfPoints) == 3.  So, last element is arrayOfPoints[index + 2]
        done = False
        stuck = 0
        while not done:
            # pick a random component and its corresponding component
            # the * ((-1) ** (random.randint(1, 2))) is to ensure that the component could be in any of the 4 quadrants
            w = random.random() * dist * ((-1) ** (random.randint(1, 2))) 
            z = math.sqrt(dist**2 - w**2) * ((-1) ** (random.randint(1, 2)))
            
            if abs(x + w) < t.screen.window_width() / 2 and abs(y + z) < t.screen.window_height() / 2: # check if the point is within the window 
                (currentX, currentY) = (x + w, y + z) # coordinates to test
                (previousX, previousY) = arrayOfPoints[len(arrayOfPoints) - 1] # last recorded point (before new point)
                for index in range(len(linearEquations) - 1):
                    (slope, intercept) = linearEquations[index] # linear equation for the points being checked
                    
                    if previousX == currentX: # no linear equation joins these points (2 y-values for the same x-value)
                        # print("Zero division error.")
                        break
                    (testSlope, testIntercept) = solveLinearEquation((previousX, previousY), (currentX, currentY)) # find the linear equation joining the points
                    if testSlope == slope: # the lines are parallel (no POI)
                        # print("Zero division error.")
                        break
                    # find the POI
                    (xi, yi) = pointOfIntersection((slope, intercept), (testSlope, testIntercept))
                    # now check where the POI is in relation to the points tested.
                    check = interceptInRange.interceptInRange((previousX, previousY), (currentX, currentY), arrayOfPoints[index], arrayOfPoints[index + 1], (xi, yi))
                    if check == -1: # if the intercept was in range, then the point is not valid
                        stuck += 1
                        break
    
                    # if the POI is not in range, and this is the last valid point to be checked, then the new point is a valid point (i.e. no POIs were in range)
                    if check == 1 and (slope, intercept) == linearEquations[len(linearEquations) - 2]: 
                        done = True
            if stuck >= 100: # don't check 100 or more points - then the walk is stuck
                break

        # if the walk has checked >= 100 new points and none are valid, then the walk is stuck
        if stuck >= 100:
            print('\nWalk stuck!  Exiting...')
            break # exit the walk

        # if the point is valid, update the position and add the new point to the record
        x += w
        y += z
        t.goto(x, y)
        arrayOfPoints += [(x, y)]
        (Slope, Intercept) = solveLinearEquation(arrayOfPoints[index + 2], arrayOfPoints[index + 3])
        linearEquations += [(Slope, Intercept)]
        

# function to find the line joining 2 points
# returns the line as (m, b) where m is the slope and b is the y-intercept
# pointA and pointB --> the 2 points to find the line between
def solveLinearEquation(pointA, pointB):
    # y = mx + b
    (ax, ay) = pointA
    (bx, by) = pointB
    m = (by - ay) / (bx - ax)
    # b = y - mx
    b = by - (m * bx)
    return (m, b)


# function to find the point of intersection between 2 lines
# returns the point as (x, y)
# each line is passed in as a tuple (m, b) where m is the slope and b is the y-intercept
# lineA and lineB --> the 2 lines to find the POI of
def pointOfIntersection(lineA, lineB):
    # y = mx + b
    # y = cx + d
    # At the POI, the x and y coordinates are the same
    # mx + b = cx + d
    # mx - cx = d - b
    # x(m - c) = d - b
    # x = (d - b) / (m - c)
    (m, b) = lineA
    (c, d) = lineB
    xi = (d - b) / (m - c)
    yi = (m * xi) + b
    return (xi, yi)


# main function controls user inputs and runs the program   
def main():
        t = Turtle()
        # prompt for user inputs
        iterations = int(input("Enter the number of reps: "))
        length = int(input("Enter the distance travelled for each step: "))
        t.pencolor("red")
        t.screen.bgcolor("black")

        # run the walk with the parameters specified
        # this walk starts at the origin (centre of the window) every time
        selfAvoidingWalk(t, 0, 0, iterations, length)
        t.hideturtle()

        print '\n\nProgram Done!'
        
main()
             
                
                
                
            
            
