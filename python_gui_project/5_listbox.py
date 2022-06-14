from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

listbox = Listbox(root, selectmode="extended", height = 0)
listbox.insert(0, "Apple")
listbox.insert(1, "StrawBerry")
listbox.insert(2, "Banana")
listbox.insert(END, "WaterMelon")
listbox.insert(END, "Grape")
listbox.pack()


def btncmd():
    #listbox.delete(0) #Delete last element

    #check number
    #print("In the list, There are ",listbox.size())

    #Check content
    #print("From first one to three : ", listbox.get(0,2))

    #Return position for values
    print("Selected content : ", listbox.curselection())

btn = Button(root, text="click", comman=btncmd)
btn.pack()

root.mainloop()