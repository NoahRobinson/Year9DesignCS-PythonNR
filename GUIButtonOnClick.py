import tkinter as tk

def onclick(args):

	if args == 1:
		print("Bus")
	if args == 2:
		print("Streetcar")

root = tk.Tk()
root.title("Bus or Streetcar")

btn1 = tk.Button(root, text = "Bus", command=lambda:onclick(1))
btn2 = tk.Button(root, text = "Streetcar", command=lambda:onclick(2))

btn1.pack()
btn2.pack()

root.mainloop()