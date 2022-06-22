import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480") # width and height

def info():
    msgbox.showinfo("Alert", "Reservation is complete.")

def warn():
    msgbox.showwarning("Warning", "Seat is sold out")

def error():
    msgbox.showerror("Error", "Payment Error happened")

def okcancel():
    msgbox.askokcancel("Confirm / Cancel", "Do you want continue?")

def retrycancel():
    response = msgbox.askretrycancel("Retry / Cancel", "Temporary Error. Do you want continue?")
    if response == 1:
        print("Retry")
    elif response == 0:
        print("Cancel")      

def yesno():
    msgbox.askyesno("Yes / No", "It is different seat. Do you want continue?") 

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Your work is not stored.\nDo you want to finish program after you save?") 

    print("Response:", response)
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")



Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="Confirm Cancel").pack()
Button(root, command=retrycancel, text="Retry Cancel").pack()
Button(root, command=yesno, text="Yes No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()
root.mainloop()