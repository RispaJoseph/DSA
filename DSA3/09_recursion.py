def recursion(i):
    print(i)
    if i == 1:
        return i
    else: 
        return recursion(i-1)

result = recursion(20)
print(result)