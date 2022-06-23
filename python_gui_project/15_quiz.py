import os
from tkinter import *

root = Tk()
root.title("Untitled - Windows ")
root.geometry("640x480") # width and height

filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)

menu_file = Menu(menu, tearoff= 0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_separator()
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit )
menu.add_cascade(label="File", menu=menu_file)


menu.add_cascade(label="Edit")
menu.add_cascade(label="Format")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()