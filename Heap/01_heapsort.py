def max_heapify(A,n,i):
    l = left(i)
    r = right(i)

    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        max_heapify(A,n,largest)



def left(i):
    return 2*i+1

def right(i):
    return 2*i+2


def build_max_heap(A):
    n = len(A)
    for i in range(n, -1, -1):
        max_heapify(A,n,i)

    for i in range(n-1,-1,-1):
        A[0],A[i] = A[i],A[0]
        max_heapify(A,n,0)

A = [34,5,2,76,0,41,8]
build_max_heap(A)
print(A)