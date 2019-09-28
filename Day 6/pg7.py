
first,second = 0,1

print(first,second,end="")

for i in range(0,28):
	third = first + second
	first,second,i = second,third,i+1
	print(" ",third,end="")

