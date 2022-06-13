from tkinter import *

root = Tk()
root.title("GUI")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="button2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button2")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="btn.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button is clicked")

btn7 = Button(root, text="Active Button", command=btncmd)
btn7.pack()

root.mainloop()