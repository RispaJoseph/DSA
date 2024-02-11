class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    def remove_duplicates(self):
        current = self.head

        while current and current.next:
            if current.data == current.next.data:
                # If duplicate, skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

# Example usage:
linked_list = LinkedList()

# Adding sorted elements
linked_list.head = Node(1)
linked_list.head.next = Node(2)
linked_list.head.next.next = Node(2)
linked_list.head.next.next.next = Node(3)
linked_list.head.next.next.next.next = Node(4)

print("Original Linked List:")
linked_list.print_list()

linked_list.remove_duplicates()

print("\nLinked List after removing duplicates:")
linked_list.print_list()
