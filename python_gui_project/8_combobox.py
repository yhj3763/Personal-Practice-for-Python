import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

values = [str(i) + "Day" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values = values)
combobox.pack()
combobox.set("Payment Day")

values = [str(i) + "Day" for i in range(1, 32)]
readonly_combobox = ttk.Combobox(root, height=10, values = values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="Selection", comman=btncmd)
btn.pack()

root.mainloop()