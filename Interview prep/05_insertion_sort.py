lst = [8, 6, 7, 2, 9, 1, 5]
print(lst)

for i in range(1,len(lst)):
    current = lst[i]
    pos = i
    while current < lst[pos-1] and pos > 0:
        lst[pos] = lst[pos-1]
        pos = pos-1
    lst[pos] = current

print(lst)
