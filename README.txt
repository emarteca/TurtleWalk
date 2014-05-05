Greetings, comrades!

The self-avoiding walk is a pretty well-known problem. 
For the walk to be self-avoiding, it must never cross its own path.

In this case, I wrote a self-avoiding walk in 2D space, represented via Python's Turtle Graphics.
As the walk progresses, the turtle draws its path across the screen.  This serves both to ensure
that the algorithm is actually working, and to visually represent the idea of the self-avoiding
walk and the speed of the algorithm.

Included in this project are also some random-walks, which follow the same basic algorithms but 
are not self-avoiding - the turtle walks randomly within the bounds of the graphics window.

The mechanics behind the self-avoiding walk are as follows:
       - draw 2 lines (i.e. 3 points)
       - keep track of all the points in the walk
       - keep track of the equations of the lines between all adjacent points
       - for the rest of the steps, before walking to a new point, ensure that
         the step between the last point and the new point does not intersect
         any of the previous steps
If the walk gets stuck for 100 tries (i.e. checking 100 points) then it exits.

So, for each set of adjacent points in the walk, the linear equation joining these is calculated. 
This is used to ensure there is no point of intersection with the line joining the last point and 
the new point to be checked with any other steps in the walk.
(Since all lines are infinite, unless they are parallel, there will always be a POI.  However, for
the steps to cross, the POI must be between all 4 points being examined).

There are several minor variations of the algorithm.  All details are commented in-code!


Future ideas:

	- Make the self-avoiding walk so there is a buffer range to avoid (i.e. the walk cannot come 
	  within a specified distance of its own path, rather than just avoiding crossing it)
	- Make a reflect-walk --> this would involve the walk reflecting off itself at the same angle
	  (i.e. the angle of reflection is equal to the angle of incidence)
	  Hopefully this would end up being a simulation for total internal reflection.



Feel free to fork the repository and change/add to it.  If you have any improvements or suggestions,
please let me know!

This was a very fun project for me, and I hope you've also enjoyed it.

Thanks! :)