import tkinter as tk
from turtle import *

def trt():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def forloop():
    for i in range (-10,10):
        print (i," ",end="")

def create_trt():
    trt()

root = tk.Tk()
root.option_add("*Font", "courier")
b = tk.Button(root, text="random chaos",font=('courier', '20') ,command=create_trt)
c = tk.Button(root, text="recursion   ",font=('courier', '20') ,command=create_trt)
b.pack()
c.pack()

root.mainloop()
