lst = [8,6,7,2,9,1,5]
print(lst)

for i in range(len(lst)):
    min_index = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i],lst[min_index] = lst[min_index],lst[i]

print(lst)