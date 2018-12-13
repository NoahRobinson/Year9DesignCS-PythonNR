import tkinter as tk


#Step 1: Create Fake Data
#This would simpulate what would be pulled from online
#The times are pulled from moovit
#Buses - Make 3 busses
bus5L = ["0603","0617","0631","0644","0657","0710","0723","0736","0749","0802","0815","0828","0841","0855","1505","1530","1550","1610","1630","1650","1710","1730","1750","1809","1827","1849","1911","1933","1955","2017","2039","2101","2123","2145","2207"] 
bus5AL = ["0630","0643","0657","0710","0723","0736","0749","0802","0815","0828","0841","0853","0906","0919","0943","1113","1143","1213","1243","1313","1343","1413","1443","1510","1541","1601","1621","1641","1701","1721","1741","1801","1818","1835","1853","1914","1935","1956","2018","2040","2102","2124","2148","2212"]
#Street Cars - Make 2 StreetCars
Streetcar512AE = ["0000","0006","0013","0020","0027","0033","0040","0047","0054","0100","0107","0114","0121","0127","0134","0141","0148","0154","0201","0206","0213","0508","0522","0533","0544","0550","0555","0600","0605","0609","0613","0621","0625","0629","0634","0639","0644","0650","0655","0700","0705","0711","0714","0716","0721","0724","0726","0730","0734","0739","0742","0745","0749","0753","0757","0800","0804","0808","0812","0815","0819","0823","0827","0830","0834","0838","0842","0845","0849","0853","0857","0900","0904","0908","0912","0915","0919","0923","0927","0930","0934","0938","0942","0945","0949","0953","0957","1000","1004","1008","1012","1015","1019","1023","1027","1030","1034","1039","1044","1049","1053","1058","1103","1108","1112","1117","1122","1127","1131","1136","1141","1146","1150","1155","1200","1205","1209","1214","1219","1224","1228","1233","1238","1243","1247","1252","1257","1302","1306","1311","1316","1321","1325","1330","1335","1340","1344","1349","1354","1359","1403","1408","1413","1418","1422","1427","1432","1437","1441","1446","1451","1456","1500","1503","1505","1510","1515","1519","1523","1527","1531","1535","1540","1544","1548","1552","1556","1600","1605","1609","1613","1617","1621","1625","1630","1634","1638","1642","1646","1650","1655","1659","1703","1707","1711","1715","1720","1724","1728","1732","1736","1740","1745","1749","1753","1757","1801","1805","1810","1814","1818","1822","1826","1830","1835","1839","1843","1847","1851","1855","1900","1904","1908","1912","1916","1920","1925","1929","1931","1936","1941","1947","1954","2001","2007","2014","2021","2028","2034","2041","2048","2055","2101","2108","2115","2122","2128","2135","2142","2149","2155","2202","2209","2216","2220","2226","2233","2239","2245","2252","2259","2306","2312","2319","2326","2333","2339","2346","2353"]
Streetcar512AW = ["0003","0010","0016","0023","0030","0037","0043","0050","0057","0104","0110","0117","0124","0131","0137","0144","0151","0158","0205","0514","0528","0539","0550","0557","0603","0608","0613","0618","0623","0628","0633","0639","0644","0649","0654","0700","0705","0710","0715","0720","0724","0727","0731","0735","0739","0742","0746","0750","0754","0757","0801","0805","0809","0812","0816","0820","0824","0827","0831","0835","0839","0842","0846","0850","0854","0857","0901","0905","0909","0912","0916","0920","0924","0927","0931","0935","0939","0942","0946","0950","0954","0958","1003","1007","1012","1017","1022","1026","1031","1036","1041","1045","1050","1055","1100","1104","1109","1114","1119","1123","1128","1133","1138","1142","1147","1152","1157","1201","1206","1211","1216","1220","1225","1230","1235","1239","1244","1249","1254","1258","1303","1308","1313","1317","1322","1327","1332","1336","1341","1346","1351","1355","1400","1405","1410","1414","1419","1424","1429","1433","1438","1443","1448","1452","1456","1501","1505","1509","1513","1517","1521","1526","1530","1534","1538","1542","1546","1551","1555","1559","1603","1607","1611","1616","1620","1624","1628","1632","1636","1641","1645","1649","1653","1657","1701","1706","1710","1714","1718","1722","1726","1731","1735","1739","1743","1747","1751","1756","1800","1804","1808","1812","1816","1821","1825","1829","1833","1837","1841","1846","1850","1854","1858","1902","1907","1912","1918","1924","1931","1938","1945","1951","1958","2005","2012","2018","2025","2032","2039","2045","2052","2059","2106","2112","2119","2126","2133","2139","2146","2153","2200","2207","2214","2221","2228","2235","2242","2249","2255","2302","2309","2316","2322","2329","2336","2343","2349","2356"]

root = tk.Tk()

root.title("TTC Around UCC")
root.configure(bg = "#737278")#a6a7a9

#Labels******************************************************************************************

titleLabel = tk.Label(root, text = "TTC Around UCC", font = ("System", 48), background = ("#737278"), foreground = ("#7d8db3"))
titleLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

Label1 = tk.Label(root, text = "Current Time in 24 Hour Clock", font = ("Helvetica", 16), bg = ("#737278"), fg = ("#ffffff"))
Label1.grid(row = 5, column = 0, columnspan = 2)
Label2 = tk.Label(root, text = "Scheduled Arrival", font = ("Helvetica", 18), bg = ("#737278"), fg = ("#ffffff"))
Label2.grid(row = 8, column = 0, columnspan = 2)

#Option Menu*************************************************************************************

def change(*args):
	print("Stop Changed")

OPTIONS = [
	"Lonsdale",
	"Avenue Road"
]

var = tk.StringVar(root)
var.set("Select Stop")
var.trace("w",change)

DropDownMenu = tk.OptionMenu(root,var,OPTIONS[0],OPTIONS[1])
DropDownMenu.grid(row = 4, column = 0, columnspan = 2)

def change(*args):
	print("Stop Changed")

TTC = [
	"5",
	"5a",
	"512"
]

var = tk.StringVar(root)
var.set("Select Bus or Streetcar")
var.trace("w",change)

DropDownMenu1 = tk.OptionMenu(root,var,TTC[0],TTC[1],TTC[2])
DropDownMenu1.grid(row = 3, column = 0, columnspan = 2)

#Text Box****************************************************************************************

text1 = tk.Text(root, height = 5, width = 25)
text1.grid(row = 9, column = 0, columnspan = 2)

#Back End****************************************************************************************
def onclick(*args):
	text1.delete('1.0', tk.END)
	if OPTIONS[0] and TTC[0]:
		text1.insert(tk.INSERT, bus5L)
		print(bus5L)
	else:
		print("no")

#Enter Button****************************************************************************************

#btn1 = tk.Button(root, background = "RoyalBlue2", text = "Enter", command = onclick)
#btn1.grid(row = 7, column = 0, columnspan = 2)

btn = tk.Button(root, text = "Enter", background = ("#a6a7a9"), command = onclick)
btn.grid(row = 7, column = 0, columnspan = 2)

def onReturn(event):
	print("Return Pressed")

	value = entry1.get();
	print(value)
	entry1.delete(0, 'end')
	





root.title("GUI Entry With Return")


entry1 = tk.Entry(root)

entry1.bind("<Return>", onReturn)

entry1.grid(row = 6, column = 0, columnspan = 2)

root.mainloop()