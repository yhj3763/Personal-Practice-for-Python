from tkinter import *

root = Tk()
root.title("GUI")

#File Frame
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Selected Remove")
btn_del_file.pack(side="right")

list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

path_frame = LabelFrame(root, text="Save Path")
path_frame.pack()

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady= 4)

btn_dest_path = Button(path_frame, text="Find", width=10)
btn_dest_path.pack(side="right")


root.resizable(False, False) # width and height are unchangable
root.mainloop()