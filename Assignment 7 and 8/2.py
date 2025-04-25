# 2. Write a Python program to create a class representing a queue data structure. Include methods
# for enqueueing and dequeuing elements.
class node:
    def __init__(self,d):
        self.data=d
        self.next=None
class queue:
    def __init__(self,MAX):
        self.size=MAX
        self.rear=-1
        self.front=-1
    def enqueue(self):
        if(self.rear==self.size-1):
            print("queue overflow")
            return
        n=int(input("enter the data to be inserted:"))
        new=node(n)
        if self.front==-1:
            self.head=new
            self.front+=1
            self.rear+=1
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new
            self.rear+=1
    def dequeue(self):
        if (self.front==-1 or self.front>self.rear):
            print("Queue under flow")
            return
        temp=self.head
        self.head=self.head.next
        print(f"{temp.data} popped")
        del temp
        self.front+=1

    def show(self):
        if(self.front==-1 or self.front>self.rear):
            print("Queue is empty")
            return
        temp=self.head
        while temp!=None:
            print(f"{temp.data} ",end="")
            temp=temp.next

n=int(input("enter the size of queue:"))
n1=queue(n)
flag=0
while True:
    ch=int(input("\nEnter your choice\n1.enqueue\n2.dequeue\n3.show queue\n4.exit\n"))
    match ch:
        case 1:
            n1.enqueue()
        case 2:
            n1.dequeue()
        case 3:
            n1.show()
        case 4:
            flag=1
    if flag==1:
        break