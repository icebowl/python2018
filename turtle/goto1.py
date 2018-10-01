import turtle  
from random import randint
w = turtle.Screen()
w.setup(800, 600)  
w.bgcolor("#000000")
t = turtle.Turtle()
t.color("#ffff00")
t.width(1)


	
def main():
	t.speed(0)
	h = randint(0,400) # Calculate a starting point for x
	k = randint(0,400) # Calculate a starting point for y
	count = 0
	while True:
		x = randint(0,400) # Assign a new x value from the list alist[] to x
		y = randint(0,400 )# Assign a new y value from the list alist[] to y
		t.penup()
		t.goto(x, y)
		t.pendown()
		t.fd(1)
		count = count + 1
		if (count > 10000000):
			break
	input("Press return to end")
	win.close()

main()


