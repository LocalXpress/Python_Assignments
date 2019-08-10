a = 3 					# Integer Type
b = 4.56				# Float Type
c = 4 + 6j
d = "Swaroop"
e = (1,2,3,4)
f = [1,2,3,4]
g = {'a':1,'b':2,'c':3,'d':4}


print("a is: ",type(a))
print("b is: ",type(b))
print("c is: ",type(c))
print("d is: ",type(d))
print("e is: ",type(e))
print("f is: ",type(f))
print("g is: ",type(g))

print(f)
f.append(5)
print(f)

#THIS IS GOING TO GIVE US AN ERROR BECAUSE TUPLE IS AN IMMUTABLE DATA TYPE
# print(e)
# e.append(5)
# print(e)

print(g[0])






