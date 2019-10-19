i,j = 0,0

while i<5:
	j = 0
	#THIS PART OF THE LOOP PRINTS SPACES
	while j<(i):
		print("   ",end="")
		j = j + 1
	
	j = 0

	#THIS PART OF THE LOOP PRINTS STARS
	while j<(5-i):
		print(" * ",end="")
		j = j + 1

	i = i + 1
	print()

print()