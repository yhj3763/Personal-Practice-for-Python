from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

#For multiple lines
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Type the text")

#for one line
e = Entry(root, width=30)
e.pack()
e.insert(0, "Type one line")

def btncmd():
    print(txt.get("1.0", END)) #1 means line 0 means column
    print(e.get())

    #Delete content
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", comman=btncmd)
btn.pack()

root.mainloop()