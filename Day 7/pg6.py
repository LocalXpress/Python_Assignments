i,j = 0,0

while i<5:
	j = 0
	#THIS PART OF THE LOOP PRINTS SPACES
	while j<(4-i):
		print("   ",end="")
		j = j + 1
	
	j = 0

	#THIS PART OF THE LOOP PRINTS STARS
	while j<(i+1):
		print(" * ",end="")
		j = j + 1

	i = i + 1
	print()

print()