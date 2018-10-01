print("0")
print("1")
print("2")
print("3")
print("4")
print("5")

print("*************************************************************")

for i in range(0, 6, 1):
	print(i)
#How the above loop will run
#We would reach line 27
# i = 0, 0 < 6, True RUN LOOP
# i = 1, 1 < 6, True RUN LOOP
# i = 2, 2 < 6, True RUN LOOP
# i = 3, 3 < 6, True RUN LOOP
# i = 4, 4 < 6, True RUN LOOP
# i = 5, 5 < 6, True RUN LOOP
# i = 6, 6 = 6, False EXIT LOOP AND MOVE ON

print("*************************************************************")

print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)

print("*************************************************************")

print("Write a loop that will print even numbers from -22 to 134 inclusive")
for i in range(-22, 135, 2):
	print(i)

print("*************************************************************")

print("We can count backwards as well. Python3 will assume the check based on")
print("relative value of the count and the check")

for i in range(3,0,-1):
	print(i)

print("*************************************************************")

print("Print out all numbers from 101 to 0 inclusive")
for i in range(101,-1,-1):
	print(i)

print("*************************************************************")

s = "Fish_food"

for i in range(0,len(s),1):
	print(s[i])

print("*************************************************************")

for i in range(-1,-1,-1):
	print(s[i])

print("*************************************************************")
for i in range(0,len(s),2):
	print(s[i])