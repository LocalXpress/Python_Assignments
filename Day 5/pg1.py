import math

w = float(input("Enter the weight: "))
h = float(input("Enter the height: "))

b = w/math.pow(h,2)

if b < 18.5:
	print("UNDERWEIGHT")
elif b>= 18.5 and b<=24.9:
	print("HEALTHY")
elif b>=25 and b<=29.9:
	print("OVERWEIGHT")
else:
	print("OBESE") 
