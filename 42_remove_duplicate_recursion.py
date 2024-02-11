def remove_duplicates(arr, index=0):
    if index == len(arr):
        return arr
    
    if arr[index] in arr[:index]:
        arr.pop(index)  
        return remove_duplicates(arr, index)
    else:
        return remove_duplicates(arr, index + 1)


arr = [1, 5, 2, 3, 4, 4, 2]
result = remove_duplicates(arr)
print("Array after removing duplicates:", result)
