# Implement Stack using List

# stack = []
# def push():
#     if len(stack) == n:
#         print("List is full!")
#     else:
#         element = input("Enter the element: ")
#         stack.append(element)
#         print(stack)


# def pop_element():
#     if not stack:
#         print("Stack is empty!")
#     else:
#         e = stack.pop()
#         print("Removed element:", e)
#         print(stack)



# n = int(input("Enter the limit of the stack : "))
# while True:
#     print("Select an operation 1.Push 2.Pop 3.Quit")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("Invalid Selection!")




# Implementing Stack using different Modules
        
# import collections
# stack = collections.deque()
# print(stack)

# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.appendleft(40)

# print(stack)

# print(stack[-1])

# stack.pop()
# stack.popleft()

# print(stack)
        



# Middle element in a stack

# class StackWithMiddle:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if not self.stack:
#             return None
#         return self.stack.pop()

#     def findMiddle(self):
#         length = len(self.stack)

#         if length == 0:
#             return None

#         middle_index = length // 2

#         return self.stack[middle_index] if length % 2 != 0 else None


# # Example usage:
# stack = StackWithMiddle()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print("Middle element:", stack.findMiddle())  # Output: 3

# stack.pop()
# print("Middle element after pop:", stack.findMiddle())  # Output: 2

class StackWithMiddle:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def findMiddle(self):
        if not self.stack:
            return None
        return self.stack[len(self.stack) // 2]

# Create an instance of StackWithMiddle
my_stack_instance = StackWithMiddle()

# Push elements onto the stack
my_stack_instance.push(1)
my_stack_instance.push(2)
my_stack_instance.push(3)
my_stack_instance.push(4)
my_stack_instance.push(5)
my_stack_instance.push(6)

# Call findMiddle on the instance
middle_element = my_stack_instance.findMiddle()

print("Middle Element:", middle_element)
