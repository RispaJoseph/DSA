def add_node(v):
    if v in graph:
        print(f"{v} already present in the graph!")
    else:
        graph[v] = []

def add_edge(v1,v2,w):
    if v1 not in graph:
        print(f"{v1} not present in the graph!")
    elif v2 not in graph:
        print(f"{v2} not present in the graph!")
    else:
        list1 = [v2,w]
        list2 = [v1,w]

        graph[v1].append(list1)
        graph[v2].append(list2)

def delete_node(v):
    if v not in graph:
        print(f"{v} is not present in the graph!")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)
        

def delete_edge(v1,v2,w):
    if v1 not in graph:
        print(f"{v1} not present in the graph!")
    elif v2 not in graph:
        print(f"{v2} not present in the graph!")
    else:
        list1 = [v2,w]
        list2 = [v1,w]

        graph[v1].remove(list1)
        graph[v2].remove(list2)


def DFS(node,graph):
    visited = set()
    if node not in graph:
        print(f"{node} not present in the graph!")
        return
    stack = []
    stack.append(node)
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)

            for i in graph[v]:
                stack.append(i[0])
    return visited

graph = {}

add_node("A")
add_node("B")
add_node("C")

add_edge("A","B",1)
add_edge("C","B",2)
add_edge("C","A",3)

# delete_node("C")

delete_edge("A","C",3)

print("DFS = ",DFS("A",graph))


print(graph)