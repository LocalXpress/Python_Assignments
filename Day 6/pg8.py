n = int(input("Enter the value: "))
k = 0
i = 2

while i<=n//2:
	if n%i == 0:
		k = 1
	i+=1

if k == 0:
	print("The number is prime!!!")
else:
	print("The number is composite!!")