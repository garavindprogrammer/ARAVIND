a='AEIOUaeiou'
b=input('Enter any string')
count=0
l=len(b)
count=[i for i in b if i in a]
print(count)
c=len(count)
print("count of vowels are :",c)
print("the percentage of vowels are :",c/len(b)*100)
