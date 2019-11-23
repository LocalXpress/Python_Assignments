import math as m
a=int(input("Enter the value of starting point:"))
b=int(input("Enter the value of ending point:"))
for i in range(a,b+1):
	for j in range(b+1):
 		if j**2==i:
 			print(i)

a=int(input("Enter the value of starting point:"))
b=int(input("Enter the value of ending point:"))

for i in range(a,b+1):
	if (m.sqrt(i)==int(m.sqrt(i))):
		print(i)
		

			




