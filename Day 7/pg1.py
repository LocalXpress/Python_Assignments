a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

c = a*b

while a!=b:
	if a>b:
		a = a-b
	else:
		b = b-a

print("GCD of the number is: ",a)
print("LCM of the number is: ",(c//a))