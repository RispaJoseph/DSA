# def reverse_stack(stack):
#     aux_stack = []
    
#     # Pop elements from the original stack and push onto the auxiliary stack
#     while stack:
#         aux_stack += (stack.pop())

#     while aux_stack:
#         stack += (aux_stack.pop())
    

# # Example usage:
# my_stack = ['R', 'I', 'S', 'P', 'A']
# print("Original Stack:", my_stack)

# reverse_stack(my_stack)

# print("Reversed Stack:", my_stack)






def Reverse_stack(stack):
    dummy_stack = []

    while stack:
        dummy_stack += stack.pop()
    
    while dummy_stack:
        stack += dummy_stack.pop()


og_stack = ['A','B','C','D','E']
print("Original Stack",og_stack)

Reverse_stack(og_stack)
print("Reversed Stack",og_stack)


    