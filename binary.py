pos = -1

def search(list,n):
    l = 0
    u = len(list)

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1



list = [3,2,5,1,50,60]
# list.sort()
# print(list)
n = 5

if search(list,n):
    print("Found at", pos+1)
else:
    print("Not Found")