# spiral_recursion_pop.py  cwc
import turtle
t = turtle.Turtle()
tWin = turtle.Screen()

def drawSpiral(t, line_length):
    t.color("#ff0000")
    t.width(1)
    if line_length > 0:
        t.forward(line_length)
        t.right(36)
        drawSpiral(t,line_length-3) # this is the recusive call to drawSpiral(t,line_length)
    t.color("#0000ff")
    t.width(1)
    #the following line uses variables from the stack of activation records (line_length)
    t.forward(line_length*-1)
    t.left(3*36)

def main():
    t.penup()
    t.goto(-100,250)
    t.pendown()
    drawSpiral(t,170)
    tWin.exitonclick()

main()

"""

I wrote this routine to model recursion and the stack of activations records.
The function drawSpiral(t,line_length-3) is called while line_length is greater
than "0".
When the condition "if line_length > 0" is false "t.forward(line_length*-1)""
is called automatically using the stack of line_length values stored in memory.
This is called popping the stack of activation records.
cwc
"""
