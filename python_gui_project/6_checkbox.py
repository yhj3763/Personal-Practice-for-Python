from tabnanny import check
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

chkvar = IntVar()
checkbox = Checkbutton(root, text="Don't show today", variable=chkvar )
#checkbox.select()
#checkbox.deselect()
checkbox.pack()

chkvar2 = IntVar()
checkbox2 =Checkbutton(root, text="Don't show for week", variable=chkvar2)
checkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : no check, 1: check
    print(chkvar2.get())

btn = Button(root, text="click", comman=btncmd)
btn.pack()

root.mainloop()