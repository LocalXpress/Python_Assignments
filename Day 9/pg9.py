x = eval(input("Enter list x: "))
y = eval(input("Enter list y: "))
z = input("Enter the operation: ")

for i in range(len(x)):
	print(eval(str(x[i])+z+str(y[i])))