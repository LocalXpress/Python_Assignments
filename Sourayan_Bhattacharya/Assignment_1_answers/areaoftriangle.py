a=int(input("Enter First side of The Triangle: "))
b=int(input("Enter Second side of The Triangle: "))
c=int(input("Enter Third side of The Triangle: "))
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))
print("The Area of the Triangle is: ",area)