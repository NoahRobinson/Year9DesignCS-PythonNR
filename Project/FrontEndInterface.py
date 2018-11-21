import tkinter as tk

def onclick(args):

	if args == 1:
		print("Bus")
	if args == 2:
		print("Streetcar")

root = tk.Tk()
root.title("Bus or Streetcar")

titleLabel = tk.Label(root, text = "TTC Around UCC", font = ("Helvitica", 16),background = "red")
titleLabel.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, text = "Bus", command=lambda:onclick(1))
btn2 = tk.Button(root, text = "Streetcar", command=lambda:onclick(2))

btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)


root.title("TTC Around UCC")

#Label1 = tk.labe(root, text = "Number:"(font = "Arial", 14))
#Label1.grid(row = 2, column = 0, columnspan = 2)

#ent1 = tk.Entry(root)
#ent1.grid(row = 3, column = 3)



root.mainloop()