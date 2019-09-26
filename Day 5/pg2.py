a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a>b and a>c:
	if b>c:
		print("a is highest,b is second highest and c is lowest")
	else:
		print("a is highest,c is second highest and b is lowest")
elif b>a and b>c:
	if a>c:
		print("b is highest,a is second highest and c is lowest")
	else:
		print("b is highest,c is second highest and a is lowest")
elif c>a and c>b:
	if a>b:
		print("c is highest,a is second highest and b is lowest")
	else:
		print("c is highest,b is second highest and a is lowest")
else:
	if a==b==c:
		print("All are equal")
	else:
		print("Two of the values are equal to each other")
