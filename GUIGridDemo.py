import tkinter as tk

#Root is a variable that holds the information
#about the main window.
#This is the window with the close,
#min, and max buttons in the top left
root = tk.Tk()

#If we want to better position the elements we
#use the grid geometry manager, not the pack.
ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)

label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0)

#Sets up your program in an infinite loop
#waiting for 
root.mainloop()