def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


arr = [1,4,6,9,45,78,89,92]
target = 19
index = binary_search(arr,target)

if index != -1:
    print(f"{target} found on {index}")
else:
    print(f"{target} not found in the list!")