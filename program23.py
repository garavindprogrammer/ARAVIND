a=list()
n=int(input("enter how many numbers :"))
for i in range(n):
    b=input('enter character :')
    a.append(b)
    print(a)
    def list_slice(s,step):
        return[s[i::step]for i in range(step)]
    c=int(input('enter the spling point: '))
    print(list_slice(a,c))
