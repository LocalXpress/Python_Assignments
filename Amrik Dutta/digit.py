x = int(input("Enter the value of x: "))

a = x%10
b = (x//10)%10
c = (x//100)


print(a)
print(b)
print(c)

z   = a+b+c
rev = (a*100)+(b*10)+c

print("The sum of the digits: ",z)
print("The reverse of the digits: ",rev)
