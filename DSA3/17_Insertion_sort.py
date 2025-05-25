def InsertionSort(list1):
    for i in range(1,len(list1)):
        current = list1[i]
        pos = i
        while current < list1[pos-1] and pos>0:
            list1[pos] = list1[pos-1]
            pos = pos-1
        list1[pos] = current

list1 = [2,4,3,5,1]
InsertionSort(list1)
print(list1)


