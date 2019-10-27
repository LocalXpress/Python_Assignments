for i in range(7):
	if i <=3:
		for j in range(i+1):
			if j == 0 or j == i:
				print(" * ",end="")
			else:
				print("   ",end="")
	else:
		for j in range(7-i):
			if j == 0 or j == (7-i-1):
				print(" * ",end="")
			else:
				print("   ",end="")
	print()