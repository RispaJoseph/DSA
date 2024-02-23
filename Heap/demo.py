def max_heapify(A,i):
    l = left(i)
    r = left(i)

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


def heapify_up(A,n):
    while n > 0:
        p = (n-1)//2
        if A[n] > A[p]:
            A[n],A[p] = A[p],A[n]
            n = p
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





def build_heap(A):
    n = len(A)//2 - 1
    for i in range(n, -1, -1):
        max_heapify(A,i)

def insert_into_heap(A,i):
    A.append(i)
    heapify_up(A,len(A)-1)



def delete_from_heap(A,val):
    if val not in A:
        print(f'{val} not present in the list!')
    else:
        pos = A.index(val)
        last = A.pop()
        A[pos] = last

        heapify_up(A,pos)
        heapify_down(A,pos)




A = [34,5,2,76,0,41,8]
build_heap(A)
print(A)

insert_into_heap(A,100)
print("Insertion = ",A)

delete_from_heap(A,0)
print("Delete = ",A)



