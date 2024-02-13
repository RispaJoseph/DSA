# Remove duplicates from an array using recursion

def remove_duplicate(A,index = 0):
    if index == len(A):
        return A

    if A[index] in A[:index]:
        A.pop(index)
        return remove_duplicate(A,index)
    else: 
        return remove_duplicate(A,index+1)


A = [1,2,3,1,2,4,4,2,5]
result = remove_duplicate(A)
print("After removing duplicate = ",result)