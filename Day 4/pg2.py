x = input("Enter the name: ")
y = int(input("Enter the marks: "))
z = int(input("Enter the class: "))

print("{name} has got {marks} in class {clas}".format(name=x,marks=y,clas=z))
print(x," has got ",y," in class ",z,sep="")