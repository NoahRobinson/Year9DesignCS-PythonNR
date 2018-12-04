import tkinter as tk


#Step 1: Create Fake Data
#This would simpulate what would be pulled from online
#Buses - Make 2 busses
bus5AL = ["0700","0720","0740","0750","0800","0810","0810","0820","0830","0840","0850","0900","0910","0920","0930","1000","1030","1100","1130","1200","1230","1300","1330","1400","1420","1440","1500","1520","1540","1600","1610","1620","1630","1640","1650","1700","1730","1800","1900","2000","2100","2300","0100"]
bus5B = ["0610","0640","0700","710","0720","0730","0740","0750","0800","0810","0810","0820","0830","0840","0850","0900","0910","0920","0930","1000","1030","1100","1130","1200","1230","1300","1330","1400","1420","1440","1500","1520","1540","1600","1610","1620","1630","1640","1650","1700","1730","1800","1900","2000","2100","2300","0100"]

#Street Cars - Make 2 StreetCars


root = tk.Tk()

root.title("TTC Around UCC")
root.configure(bg = "#4a4f50")

#Labels******************************************************************************************

titleLabel = tk.Label(root, text = "TTC Around UCC", font = ("Helvetica", 24), background = ("#4a4f50"), foreground = ("#ffffff"))
titleLabel.grid(row = 0, column = 0, columnspan = 2)

Label1 = tk.Label(root, text = "Number:", font = ("Helvetica", 16), bg = ("#4a4f50"), fg = ("#ffffff"))
Label1.grid(row = 3, column = 0, columnspan = 2)
Label2 = tk.Label(root, text = "Scheduled Arrival", font = ("Helvetica", 18), bg = ("#4a4f50"), fg = ("#ffffff"))
Label2.grid(row = 7, column = 0, columnspan = 2)

#Buttons*****************************************************************************************

def onclick(args):

	if args == 1:
		print("Bus")
	if args == 2:
		print("Streetcar")
	if args == 3:
		print("Submitted")

btn1 = tk.Button(root, text = "Bus", command=lambda:onclick(1), highlightbackground = "#4a4f50")
btn2 = tk.Button(root, text = "Streetcar", command=lambda:onclick(2), highlightbackground = "#4a4f50")
btn3 = tk.Button(root, text = "Submit", command=lambda:onclick(3), highlightbackground = "#4a4f50")

btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 6, column = 0, columnspan = 2)

#Entry Box***************************************************************************************

def onReturn(event):
	print("Return Pressed")

	value = entry1.get();
	print(value)
	entry1.delete(0,)

entry1 = tk.Entry(root, highlightbackground = "#4a4f50")

entry1.bind("<Return>", onReturn)
entry1.grid(row = 4, column = 0, columnspan = 2)

#Option Menu*************************************************************************************

def change(*args):
	print("Stop Changed")

OPTIONS = [
	"Lonsdale",
	"Avenue Road",
]

var = tk.StringVar(root)
var.set("Select Stop")
var.trace("w",change)

DropDownMenu = tk.OptionMenu(root,var,OPTIONS[0],OPTIONS[1])
DropDownMenu.grid(row = 5, column = 0, columnspan = 2)

#Text Box****************************************************************************************

text1 = tk.Text(root, height = 4, width = 25)
text1.grid(row = 8, column = 0, columnspan = 2)



root.mainloop()