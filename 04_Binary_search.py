pos = -1

def search(list,n):
    l = 0
    u = len(list)

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1


list = [10,20,30,40,50,60]
n = 10


if search(list,n):
    print("Found at ", pos+1)
else:
    print("Not Found")

