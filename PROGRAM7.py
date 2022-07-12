n=int(input('enter a number :'))
print("the divisors of %d are :"%(n))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        
