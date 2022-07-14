class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self,head):
        self.head=head
    def insertbegin(self,node):
        node.next=self.head.next
        self.head=node
        print(node.data,'inserted successfully in beginning')
        
    def insertpos(self,node,pos):
        if pos==1:
            node.next=self.head.next
            self.head=node
        else:
            prev=self.head
            for i in range(1,pos-1):
                prev=prev.next
                node.next=prev.next
                #node.next=temp.next
                print(node.data,'inserted successfully at %d position' %pos)
                
    def insertend(self,node):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=node
        print(node.data,'inserted successfully at the end')
        
    def display(self):
        temp=self.head
        #print("td=",temp.next)
        if temp.data is None:
            print("List is empty")
        else:
            while temp.next is not None:
                print(temp.data,"->",end=" ")
                temp=temp.next
                print(temp.data)
                
n1=node(20)
l1=linkedlist(n1)
#l1=display()
l1.insertbegin(node(10))
l1.insertend(node(30))
l1.insertend(node(40))
l1.insertend(node(50))
l1.display()
l1.insertpos(node(22),1)
l1.display()
l1.insertpos(node(21),3)
l1.display()
l1.insertpos(node(55),5)
l1.display() 
