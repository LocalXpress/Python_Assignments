i,j = 0,0

while i<5:
	j = 0
	while j<(5-i):
		print(" * ",end="")
		j = j + 1
	i = i + 1
	print()

print()

for i in range(5):
	for j in range(5-i):
		print(" * ",end="")
	print()