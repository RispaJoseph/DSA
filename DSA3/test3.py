def remove_duplicate(s):
    index = len(A)
    stack = []

    for i in stack:
        if i[index] not in i[:index]:
            stack.pop(i)

    remove_duplicate(A)
    return stack

A = [1,2,3,4,3,5,4]
res = remove_duplicate(A)
print(res)
