i,j = 0,0

while i<5:
	j = 0
	while j<(4-i):
		print("   ",end="")
		j = j + 1
	print(" * ",end="")
	i = i + 1
	print()
