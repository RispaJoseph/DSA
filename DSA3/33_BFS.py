def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v]= []

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        # list1 = [v2]
        # list2 = [v1]

        graph[v1].append(v2)
        graph[v2].append(v1)


def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)

def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in graph")
    elif v2 not in graph:
        print(v2,"is not present in graph")
    else:
        list1 = [v2]
        list2 = [v1]


        if list1 in graph[v1]:
            graph[v1].remove(list1)
            graph[v2].remove(list2)

import collections
def BFS(node,graph):
    visited=set()
    if node not in graph:
        print("node not present")
        return
    queue=collections.deque([node])
  
    while queue:
        current=queue.popleft()
        visited.add(current)
        for i in graph[current]:
            if i not in visited:
                queue.append(i)
        
    return visited


graph = {}
# visited = set()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
# add_node("E")

add_edge("A","B")
add_edge("A","D")
add_edge("A","C")
# add_edge("B","D")
print()
print(graph)
print()


bfs = BFS("A",graph)
print("BFS :",bfs)
