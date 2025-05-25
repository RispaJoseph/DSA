# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):
#         # Find the minimum element in the unsorted part of the array
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         # Swap the found minimum element with the first element
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# # Example usage:
# arr = [64, 25, 12, 22, 11]
# print("Original Array:", arr)

# selection_sort(arr)

# print("Sorted Array:", arr)


list1 = [56,3,2,78,6,0]
print(list1)

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_index = list1.index(min_val)
    list1[i], list1[min_index] = list1[min_index],list1[i]

print(list1)