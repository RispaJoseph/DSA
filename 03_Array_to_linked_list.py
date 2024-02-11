class Node:
  def __init__(self,data,ref=None):
    self.data=data
    self.ref=ref
    
node1=Node("1")
node2=Node("2")
node3=Node("3")

node1.ref=node2
node2.ref=node3

current_node =node1
l=[]
while current_node is not None:
  l.append(current_node.data)
  if current_node.ref is None:
    break
  else:
    current_node=current_node.ref
print(l)
  
  
  
  
# ..........................................array to linkdlist.............................................

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None

    # Create the first node
    head = ListNode(arr[0])
    current = head

    # Iterate through the array, adding nodes to the linked list
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
my_array = [1, 2, 3, 4, 5]
linked_list_head = array_to_linked_list(my_array)
print_linked_list(linked_list_head)