
for i in range(5):
        if i<=2:
                for j in range(2-i):
                        print(" ",end="")
                for j in range(2*i+1):
                        print("*",end="")
                print()        
        else:
                for j in range(i-2):
                        print(" ",end="")
                for j in range(9-2*i):
                        print("*",end="")
                print()
print("------------------------------------")                

for i in range(5):
        if i<=2:
                for j in range(2-i):
                        print(" ",end="")
                for j in range(2*i+1):
                        if j==0 or j==2*i :
                                print("*",end="")
                        else:
                                print(" ",end="")
                print()        
        else:
                for j in range(i-2):
                        print(" ",end="")
                for j in range(9-2*i):
                        if j==0 or j==(9-(2*i)-1):
                                print("*",end="")
                        else:
                                print(" ",end="")
                print()                
print("------------------------------------")

for i in range(5):
        if i<=2:
                for j in range(2-i):
                        print(" ",end="")
                for j in range(2*i+1):
                        if j%2==0:
                                print("*",end="")
                        else:
                                print(" ",end="")        
                                
                print()        
        else:
                for j in range(i-2):
                        print(" ",end="")
                for j in range(9-2*i):
                        if j==0 or j==(9-(2*i)-1):
                                print("*",end="")
                        else:
                                print(" ",end="")
                print()                
print("------------------------------------")


               
                
         
