"""
Code and algorithm by Craig Coloeman
I created this Sierpinski's Triangle without looking at other code.
I wanted to figure this out as I did my version of the Ulam spiral.

Imagine 3 vertices of a triangle which are lableled 0,1, and 2.
You pick a a random point anywhere inside of the drawing window.
Then you randomly pick one of the three triangle vertices.
The next point will then be half way between the triangle vertex and 
the first random point.  This is the new point. Pick another random
vertex and the new point will be half the distance. If this is done 
thousands of times you will get the Sierpinski's Triangle .

What I am working on now is trying to optimize the algorithm or the 
equation to fill in the triangles pattern quicker.

Please read this code and run it.  
Change it in some way.

"""
import turtle  
w = turtle.Screen()
w.bgcolor("#000000")
t = turtle.Turtle()
t.color("#ffff00")
t.width(1)

from random import randint

def newpoint(plist):  # Define a function called newpoint
	vx =[0,300,-300]  # Set the x values for triangle vertices.
	vy =[300,-100,-100]  # Set the y values for triangle vertices.
	px = plist[0] # Get the x value of a point
	py = plist[1] # Get the y value of a point
	random_point = randint(0,3) #Get one of 3 points.
	# Calculate half the distance from the current point to a triangle vertex.
	if (random_point % 3 == 0):
		plist[0] = int((px + vx[0])/2)
		plist[1] = int((py + vy[0])/2)
	if (random_point % 3 == 1):
		plist[0] = int((px + vx[1])/2)
		plist[1] = int((py + vy[1])/2)
	if (random_point % 3 == 2):
		plist[0] = int((px + vx[2])/2)
		plist[1] = int((py + vy[2])/2)
	print(plist,end='')  #print the new point
	return plist #Send the point (list) back to the calling function.
	
def main():
	t.speed(0)
	h = randint(-10,10) # Calculate a starting point for x
	k = randint(-10,10) # Calculate a starting point for y
	alist =[h,k] # Assign the starting points to a list.
	count = 0
	while True:
		alist = newpoint(alist) # Get a new point from a function that is half way between the current point and a random vertex of a triangle.
		x = alist[0] # Assign a new x value from the list alist[] to x
		y = alist[1] # Assign a new y value from the list alist[] to y
		t.penup()
		t.goto(x, y)
		t.pendown()
		t.fd(1)
		count = count + 1
		if (count > 100000):
			break
	input("Press return to end")
	win.close() # ?

main()

