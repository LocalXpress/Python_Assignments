k = 1

for i in range(5):
	for j in range(i+1):
		print(" "+str(k%2)+" ",end=" ")
		k = k + 1
	print()