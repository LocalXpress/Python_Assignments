k,p = 0,0 

for i in range(5):
	for j in range(4-i):
			print("   ", end="")
	if i%2 == 0:
		for j in range(i+1):
			print(" "+chr(ord('Z')-p)+" ", end="")
			p = p + 1
	else:
		for j in range(i+1):
			print(" "+chr(ord('A')+k)+" ", end="")
			k = k + 1
	print()
		
		
