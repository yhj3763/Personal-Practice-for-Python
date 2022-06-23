import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

Label(root, text="Choose the menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Ham Burger").pack()
Button(frame_burger, text="Cheese Burger").pack()
Button(frame_burger, text="Chicken Burger").pack()

frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Cola").pack()
Button(frame_drink, text="Cider ").pack()


root.mainloop()