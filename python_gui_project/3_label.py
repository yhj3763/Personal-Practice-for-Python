from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file ="btn.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you again")

    global photo2
    photo2 = PhotoImage(file ="label.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command = change)
btn.pack()

root.mainloop()