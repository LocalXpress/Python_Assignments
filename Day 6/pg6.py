i = 0
first,second = 0,1

print(first,second,end="")

while i < 28:
	third = first + second
	first,second,i = second,third,i+1
	print(" ",third,end="")

