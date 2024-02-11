import sys

sys.setrecursionlimit(10)
print(f"The limit is {sys.getrecursionlimit()}")

i = 0

def greet():
    global i
    i += 1
    print("hello", i)
    greet()

greet()