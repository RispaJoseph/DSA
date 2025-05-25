def higest_num(lst):
    if not lst:
        return None
    
    highest = lst[0]
    i = 1

    while i < len(lst):
        if lst[i] > highest:
            highest = lst[i]
        i+=1

    return highest


lst = [8, 6, 7, 2, 9, 1, 5]
print(higest_num(lst))