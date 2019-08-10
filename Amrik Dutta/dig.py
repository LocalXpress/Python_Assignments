import math

x   = int(input("Enter the digits: "))
s 	= x
sum = 0
rev = 0
arm = 0

while x > 0:
	sum = sum + (x%10)
	rev = (rev*10) + (x%10)
	arm = arm + math.pow((x%10),3)
	x = x//10

print("Sum of the digits: ",sum)
print("Reverse of the digits: ",rev)

if s == rev:
	print("Palindrome!!!")
else:
	print("Not Palindrome!!")

if s == arm:
	print("Armstrong!!!")
else:
	print("Not Armstrong!!")
