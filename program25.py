from collections import Counter
a=list()
b=list()
n=int(input("Enter size of 1st list: "))
for i in range(n):
 c=input("Enter strings: ")
 a.append(c)
print("The 1St list is: ",a)
n1=int(input("Enter size of 2nd list: "))
for i in range(n1):
 c=input("Enter strings: ")
 b.append(c)
print("The 2nd list is: ",b)
a[-1:]=b
print("The resultant list is: ",a)
