# Reading an integer and counting the number of digits
count=0
a= int(input(" Enter the number : "))
b=a
if (a==0):
    count=1
if(a>0):
    while(a>0):
        a=a//10
        count=count+1
else:
    while(a<0):
        a=a//10
        count=count+1
print(" The number of digits is ",count)

new_num=(count*10)+(b//(10**(count-1)))
print("The number formed is ",new_num)

        
        
