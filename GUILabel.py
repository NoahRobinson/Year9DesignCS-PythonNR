import tkinter as tk

root = tk.Tk()
root.title("GUI Label")

Label1 = tk.Label(root, text = "Number of Bus or Streetcar")
Label1.config(font= "Times 20")
Label1.pack

ent1 = tk.Entry(root)
ent1.pack