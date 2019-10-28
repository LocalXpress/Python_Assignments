# Finding number of digits
count=0
a=int(input("Enter any number : "))
b=a
c=a
d=a
if( b==0):
    count=1
if(b>0):
    while(b>0):
        b=b//10
        count=count+1        
else:
    while(b<0):
        b=b//10
        count=count+1
print("The number of digits of the given number is ",count)
print("-------------------------------------")

# Finding sum of digits 
sum=0
for i in range(count):
    sum=sum+(a%10)
    a=a//10
print("The sum of digits is ",sum)
print("-------------------------------------")

# Finding reverse of a number 

rem=0
num=0
for i in range(count):
    k=c%10
    num=num+(k*(10**((count-1)-i)))
    c=c//10
print("The reverse of the number is ",num)
print("-------------------------------------")

# Palindrome check

if(num==d):
    print("The number is palindrome ")
else:
    print("The number is not palindrome ")
    


    
