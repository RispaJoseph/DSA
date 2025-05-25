def second_highest(numbers):
    if len(numbers) < 2:
        return None
    
    highest = second_highest = float('-inf')
    i = 0

    while i < len(numbers):
        num = numbers[i]

        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num
        
        i+=1

    if second_highest == float('-inf'):
        return None
    return second_highest


numbers = [7,5,8,3,19,4,10,2]
print(second_highest(numbers))