def highest_num(lst):
    if not lst:
        return None
    
    highest = lst[0]

    for num in lst:
        if num > highest:
            highest = num
    return highest


lst = [9,8,1,5,7,10,6,2]
print(highest_num(lst))