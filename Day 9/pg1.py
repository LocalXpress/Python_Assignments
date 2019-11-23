import factorial as f

x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
	sum=sum+(x**n)/n
print(sum)	

x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
sum=0
for i in range(1,n+1):
	sum=sum+((-1)**(i+1))*(x**i)/(f.factorial(i))
print(sum)
