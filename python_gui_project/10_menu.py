import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height



def btncmd():
    pass

btn = Button(root, text="Stop", comman=btncmd)
btn.pack()



root.mainloop()