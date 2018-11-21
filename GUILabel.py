import tkinter as tk

root = tk.Tk()
root.title("GUI Label")

Label1 = tk.Label(root, text = "Number of Bus or Streetcar")
Label1.grid(row = 0 , column = 1)


ent1 = tk.Entry(root)
ent1.pack

root.mainloop()