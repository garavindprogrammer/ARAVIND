import cmath
import math
a=int(input('enter x^2 coefficient :'))
b=int(input('enter x coefficient :'))
c=int(input('enter constant'))
print("the quadratic equation is",a,"x^2+",b,"x+",c,"=0")
d=math.pow(b,2)-4*a*c
def f1(a,b,c):
  sol1=(-b-(cmath.sqrt(d)))/(2*a)
  print('one root of the equation is:',sol1)
  sol2=(-b+(cmath.sqrt(d)))/(2*a)
  print('another root of equation is:',sol2)
f1(a,b,c)
