def min_heapify(A,i):
    l = left(i)
    r = right(i)

    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i

    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        A[smallest],A[i] = A[i],A[smallest]
        min_heapify(A,smallest)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def build_min_heap(A):
    n = len(A) // 2 -1
    for i in range(n, -1, -1):
        min_heapify(A,i)


A = [34,5,2,76,0,41,8]
build_min_heap(A)
print(A)