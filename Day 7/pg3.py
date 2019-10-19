i,j = 0,0

while i<5:
	j = 0
	while j<(i+1):
		print(" * ",end="")
		j = j + 1
	i = i + 1
	print()

print()

for i in range(5):
	for j in range(i+1):
		print(" * ",end="")
	print()