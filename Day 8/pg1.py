for i in range(5):
	if i == 0 or i == 4:
		print(" * "*5,end="")
	else:
		print(" * ",end="")
		print("   "*3,end="")
		print(" * ",end="")
	print()