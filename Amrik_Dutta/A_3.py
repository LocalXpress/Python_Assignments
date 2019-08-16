print("Program to find area of a triangle when three sides are given")
a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangle: "))
c = float(input("Enter third side of the triangle: "))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f  ' %area)
