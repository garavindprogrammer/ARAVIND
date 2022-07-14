from collections import counter
a=list()
b=list()
n=int(input("enter size of 1st list :"))
for i in range(n):
    c=input("enter strings: ")
    a.append(c)
    n1=int(input("enter size of 2nd list :"))
    for i in range(n1):
        c=input("Enter strings :")
        b.append(c)
        counter1=counter(a)
        print(counter1)
        counter2=counter(b)
        print(counter2)
    print("the difference between first list and second list is :',list(counter1-counter2))
    print("the differences between secondlist and first list is :',list(counter2-counter1))      
