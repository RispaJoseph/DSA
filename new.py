def binary_search(A,target):
    l = 0
    h = len(A) - 1
    mid = (l+h)/2

    while l < h:
        if target == mid:
            return mid
        elif target > mid:
            l = mid + 1
        else:
            h = mid -1
    return -1



A = [3,5,8,19,33,40]
target = 19
result = binary_search(A,target) 

if result != -1:
    print(result)
else:
    print("Not found!")

