import tkinter as tk
import math
def submit():

	print("Submitpressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is:"+str(v)+" units cubed\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")

root = tk.Tk()
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()
output.config(state="disabled")

def onReturn(event):
	print("Return Pressed")

	value = entry1.get();
	print(value)
	entry1.delete(0, 'end')


root = tk.Tk()
root.title("GUI Entry With Return")


entry1 = tk.Entry(root)

entry1.bind("<Return>", onReturn)

entry1.pack()

root.mainloop()