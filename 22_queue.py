# # pgm 1

# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)

# queue.pop(0)
# queue.pop(0)
# queue.pop(0)
# print(queue)



# # pgm 2

# queue = []
# queue.insert(0,100)
# queue.insert(0,200)
# queue.insert(0,300)
# print(queue)

# queue.pop()
# queue.pop()
# queue.pop()
# print(queue)



# # pgm 3

# queue = []
# def enqueue():
#     element = input("Enter the element: ")
#     queue.append(element)
#     print(element,"is added to the queue!")

# def dequeue():
#     if not queue:
#         print("Queue is empty!")
#     else:
#         e = queue.pop(0)
#         print("Removed element",e)

# def display():
#     print(queue)

# while True:
#     print("Select the operation 1.Add 2.Remove 3.Show 4.Quit : ")
#     choice = int(input())
#     if choice == 1:
#         enqueue()
#     elif choice == 2:
#         dequeue()
#     elif choice == 3:
#         display()
#     elif choice == 4:
#         break
#     else:
#         print("Invalid Choice!")


# pgm 4

# import collections
# q = collections.deque()
# q.append(10)
# q.append(20)
# q.append(30)
# print(q)


# # q.popleft()
# # q.popleft()
# # q.popleft()
# print(q)
# print(q[-1])


# print(not q)





# pgm 5

import queue
q = queue.Queue()
print(q)
q.put(10)
q.put(50)
q.put(30)
print(q)

print(q.get())
print(q)



# Priority Queue

q = []
q.append(10)
q.append(5)
q.append(40)
q.append(20)
q.sort()
print(q)

q.pop(0)
q.pop(0)

print(q)




# pgm 6

import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)
print(q)

print(q.get())
print(q.get())



# Priority Queue using tuple

q = []
q.append((1,"rispa"))
q.append((4,"joseph"))
q.append((2,"ann"))

q.sort(reverse=True)

print(q)

q.pop(0)

print(q)