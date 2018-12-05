import tkinter as tk


#Step 1: Create Fake Data
#This would simpulate what would be pulled from online
#Buses - Make 3 busses
bus5L = ["0603","0617","0631","0644","0657","0710","0723","0736","0749","0802","0815","0828","0841","0855","1505","1530","1550","1610","1630","1650","1710","1730","1750","1809","1827","1849","1911","1933","1955","2017","2039","2101","2123","2145","2207"] 
bus5AL = ["0630","0643","0657","0710","0723","0736","0749","0802","0815","0828","0841","0853","0906","0919","0943","1113","1143","1213","1243","1313","1343","1413","1443","1510","1541","1601","1621","1641","1701","1721","1741","1801","1818","1835","1853","1914","1935","1956","2018","2040","2102","2124","2148","2212"]
#Street Cars - Make 2 StreetCars
Streetcar512AE = ["0000","0006","0013","0020","0027","0033","0040","0047","0054","0100","0107","0114","0121","0127","0134","0141","0148","0154","0201","0206","0213","0508","0522","0533","0544","0550","0555","0600","0605","0609","0613","0621","0625","0629","0634","0639","0644","0650","0655","0700","0705","0711","0714","0716","0721","0724","0726","0730","0734","0739","0742","0745","0749","0753","0757","0800","0804","0808","0812","0815","0819","0823","0827","0830","0834","0838","0842","0845","0849","0853","0857","0900","0904","0908","0912","0915","0919","0923","0927","0930","0934","0938","0942","0945","0949","0953","0957","1000","1004","1008","1012","1015","1019","1023","1027","1030","1034",""]

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