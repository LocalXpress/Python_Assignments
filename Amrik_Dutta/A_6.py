print("program to show three digit number")
n = int(input("Enter the single digit number between 1-7:  "))
tn = (n*100)+((n+1)*10)+(n+2)
if n>7 :
	print("Number is greater than seven!! ")
else :
	print("The three digit number is: ",tn)
