a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

sum1 = a + b + c

if a == b == c:
	sum2 = a
elif a == b and a != c:
	sum2 = c + a
elif a == c and c != b:
	sum2 = b + c
elif b == c and b != a:
	sum2 = a + b
else:
	sum2 = a + b + c

print("The sum of elements is: ",sum1)
print("The sum of non-duplicate element is: ",sum2)