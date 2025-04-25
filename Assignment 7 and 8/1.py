# Write a Python program to create a class representing a linked list data structure. Include
# methods for displaying linked list data, inserting and deleting nodes.
class node:
    def __init__(self,d):
         self.data=d
         self.next=None

class Linked_list:

    def __init__(self):
        self.head = None

    def createnode(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def deletenode(self,n):
        count=1
        temp=self.head
        if n==1:
            self.head=self.head.next
            del temp
        else:
            while(count!=n-1):
                temp=temp.next
                count+=1
            current=temp.next
            temp.next=temp.next.next
            del current
        global nodes
        nodes-=1
        
    def display(self):
        temp=self.head
        while(temp):
            print(f"{temp.data}",end=" ")
            temp=temp.next
        
c=Linked_list()
global nodes
nodes=int(input("enter num of nodes u want to create:"))
for i in range(0,nodes):
    num=int(input(f"enter data inside node {i+1}:"))
    c.createnode(num)
c.display()
n=int(input("\nenter the node u want to delete:"))
if(n>nodes or n<1):
    print("Invalid node!")
else:
    c.deletenode(n)
print("after updating:")
c.display()
