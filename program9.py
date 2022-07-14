a=int(input('enter a  first number :'))
b=int(input('enter a second number :'))
hcf=1
for i in range(1,a+1):
    if(a%i==0 and b%i==0):
      hcf=i
      lcm=int(a*b)/(hcf)
      print("The LCM of two numbers :",lcm)
    
