#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("#00ff00")
cr = turtle.Pen()
cr.color("#ffffff")

def sqrfunc(size):
	cr.width(size/10)
	for i in range(4):
		cr.fd(size)
		cr.left(90)
		size = size + 5
        
sqrfunc(10)
cr.color("#ffff00")
sqrfunc(20)
cr.color("#00ff00")
sqrfunc(30)
cr.color("#ff0000")
sqrfunc(40)
cr.color("#00f3300")
sqrfunc(50)
cr.color("#007fff")
sqrfunc(60)
cr.color("#ffff00")
sqrfunc(70)
sqrfunc(80)
holdit = input();
