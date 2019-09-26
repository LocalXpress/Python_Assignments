import random

num = random.randint(100,1000)

print("The original number is: ",num)

a 	= num%10
num	= num//10
b   = num%10
c 	= num//10

rev = a*100 + b*10 + c

print("The reverse of the number is: ",rev)