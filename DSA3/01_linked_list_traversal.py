class Node:
  def __init__(self,data):
    self.data=data
    self.ref=None
    
class Linkdlist:
  
  def __init__(self):
    self.head=None
  def print_ll(self):
    if self.head is None:
      print("Empty")
    else:
      n=self.head
      while n is not None:
        print(n.data)
        n=n.ref
        
  # add data at begining
  
  def add_begin(self,data):
    new_node=Node(data)
    new_node.ref=self.head
    self.head=new_node
    
    
  # add data at end
  
  def add_end(self, data):
    new_node=Node(data)
    # check if linkdlist is empty
    if self.head is None:
      self.head=new_node
    else:
      n=self.head
      while n.ref is not None:
        n=n.ref
      n.ref=new_node
  
  def add_after(self,data,x):
    n = self.head
    while n is not None:
      if x == n.data:
        break
      n = n.ref
    if n is None:
      print("Node is not present in LL")
    else:
      new_node = Node(data)
      new_node.ref = n.ref
      n.ref = new_node


  def add_before(self,data,x):
    if self.head is None:
        print("Linked List is empty!")
        return
    if self.head.data==x:
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        return
    n = self.head
    while n.ref is not None:
        if n.ref.data==x:
            break
        n = n.ref        
    if n.ref is None:
        print("Node is not found!")
    else:
        new_node = Node(data)
        new_node.ref = n.ref
        n.ref = new_node
  

  def delete_by_value(self,x):
    if self.head is None:
      print("Can't delete L is empty")
      return
    if x == self.head.data:
      self.head = self.head.ref
      return
    n = self.head
    while n.ref is not None:
      if x == n.ref.data:
        break
      n = n.ref
    if n.ref is None:
      print("Node is not present")
    else:
      n.ref = n.ref.ref




    
    
l1=Linkdlist()
l1.add_begin(580)
l1.add_begin(58)
l1.add_end(70)
l1.add_after(1000,58)
l1.add_before(300,580)
l1.delete_by_value(70)
l1.print_ll()




