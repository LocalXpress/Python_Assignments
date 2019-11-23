import hcf as f
a=int(input("Enter the value of starting point:"))
b=int(input("Enter the value of ending point:"))
for i in range(a,b+1):
	for j in range(i+1,b+1):
		if (f.hcf(i,j)==1):
			print(i,j)