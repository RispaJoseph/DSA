def linear_serach(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return 

arr = [5,8,1,2,3,6,9]
target = 4

print(f"{target} is found on index",linear_serach(arr,target))