# pos = -1

# def search(list,n):
#     i = 0
#     while i < len(list):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i += 1




# list = [5,8,4,6,9,2]
# n = 9



# if search(list,n):
#     print("Found at ", pos+1)
# else:
#     print("Not Found")





# .....................Linear search using for loop..................................................
# pos = -1
# def search(list,n):
#     for i in range(len(list)):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#     return False



# list = [5,8,4,6,9,2]
# n = 6


# if search(list,n):
#     print("Found at ", pos)
# else:
#     print("Not Found")





# ............................Linear search............................................

def linear_search(list,target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1




list = [4,6,8,9,10]
target = 6

result = linear_search(list,target)

if result != -1:
    print(f"Element {target} found at index {result+1}")
else:
    print(f"Element {target} not found!")


# .......................................Example..........................................

# def linear_search(list,t):
#     for i in range(len(list)):
#         if list[i] == t:
#             return True 
#     return False



# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target_value = 7


# if linear_search(my_list, target_value):
#     print(f"Element {target_value} is present at index")
# else:
#     print("Not found!")