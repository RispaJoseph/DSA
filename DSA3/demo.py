class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def Print_LL(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->", end= " ")
                n = n.ref
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
            
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def add_before(self,data,x):
        if self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("The node is not present in the LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")
            
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty, you can't delete")
        else:
            self.head = self.head.ref
        
    def delete_end(self):
        if self.head is None:
            print("The linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            
        
            
            
    
            
LL1 = LinkedList()
LL1.add_begin(20)
LL1.add_begin(10)

LL1.add_after(30,20)
LL1.add_before(40,30)
LL1.add_end(50)

LL1.insert_empty(5)
LL1.insert_empty(10)

LL1.delete_begin()
LL1.delete_end()

LL1.Print_LL()