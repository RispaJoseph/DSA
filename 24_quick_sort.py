def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage:
arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted Array:", sorted_arr)
