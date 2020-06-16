number = int(input("Enter the number you want the table for:\n"))
print("Here is the table of " + str(number) + "\n")

for i in range(1, 11):
	print(str(number) + ' x ' + str(i) + ' = ' + str(number * i))