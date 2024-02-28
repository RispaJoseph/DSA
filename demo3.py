def heapify(arr,n,i):
    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,n,largest)


def left(i):
    return 2*i+1

def right(i):
    return 2*i+2


def build_heap(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

arr = [4, 10, 3, 5, 1]
build_heap(arr)
print(arr)