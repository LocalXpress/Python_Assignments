lc,lu,la,ld,ls = 0,0,0,0,0

x = "3ArkaJiT1#"
i = 0

for i in range(len(x)):
	if x[i].isupper():
		lu = lu + 1
	if x[i].islower():
		lc = lc + 1
	if x[i].isalpha():
		la = la + 1
	if x[i].isdigit():
		ld = ld + 1
	if not x[i].isupper() and not x[i].islower() and not x[i].isalpha() and not x[i].isdigit():
		ls = ls + 1

print("Number of upper case letters: ",lu)
print("Number of lower case letters: ",lc)
print("Number of alphabets: ",la)
print("Number of digits: ",ld)
print("Number of special case: ",ls)


