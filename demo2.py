def heapify(A,n,i):
    l = left(i)
    r = right(i)

    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r < n and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A,n,largest) 




def left(i):
    return 2*i+1


def right(i):
    return 2*i+2

def build_heap(A):
    n = len(A)
    for i in range(n,-1,-1):
        heapify(A,n,i)

    for i in range(n-1,-1,-1):
        A[i],A[0] = A[0],A[i]
        heapify(A,i,0)


A = [5,9,6,1,8,10,2,4,7,3]
build_heap(A)
print(A)
    