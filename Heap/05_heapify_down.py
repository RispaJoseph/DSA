def max_heapify(A,i):
    l = left(i)
    r = right(i)

    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        max_heapify(A,largest)

    
def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def heapify_up(A,i):
    while i > 0:
        p = (i-1)//2
        if A[i] > A[p]:
            A[i],A[p] = A[p],A[i]
            i = p
        else:
            break

    
def heapify_down(A,i):
    while True:
        l = left(i)
        r = right(i)

        if l < len(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < len(A) and A[r] > A[largest]:
            largest = r

        if largest != i:
            A[largest],A[i] = A[i],A[largest]
        else:
            break




def delete_from_heap(A,val):
    if val not in A:
        print(f'{val} not found in the heap')
    else:
        pos = A.index(val)
        last = A.pop()

        A[pos] = last

        heapify_down(A,pos)
        heapify_up(A,pos)


# def delete_max(A):
#     last = A.pop()
#     A[0] = last
#     heapify_down(A,0)


def build_heap(A):
    n = len(A)
    for i in range(n, -1, -1):
        max_heapify(A,i)



A = [34,5,2,76,0,41,8]
build_heap(A)
print(A)

delete_from_heap(A,41)
print(A)

# delete_max(A)
# print(A)