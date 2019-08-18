P=int(input("Enter the Principal amount:  "))
R=int(input("Enter the rate of interest:  "))
T=int(input("Enter the time: "))

SI=(P*R*T)/100
n=(int(input("Enter number of times:")))
CI=P(1+R/n)^nT
print("the simple interest is ",SI)
print("the compound interest is",CI)
