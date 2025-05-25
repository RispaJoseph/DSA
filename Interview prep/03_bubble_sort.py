lst = []
num = int(input("Enter your range: "))
for i in range(num):
    lst.append(int(input()))


for j in range(len(lst)-1):
    for i in range(len(lst)-1-j):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)