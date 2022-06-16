from tabnanny import check
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

label1 = Label(root, text="Select Menu").pack()


burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="HamBurger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="CheeseBurger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="ChickenBurger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


label2 = Label(root, text="Select Drink").pack()


drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Cola", value="Cola", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Cidar", value="Cidar", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) 
    print(drink_var.get()) 

btn = Button(root, text="click", comman=btncmd)
btn.pack()

root.mainloop()