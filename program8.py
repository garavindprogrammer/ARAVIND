a=int(input('enter first number'))
b=int(input('enter second number'))
hcf=1
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
        hcf=i
        print("hcf of two numbers are :",hcf)
