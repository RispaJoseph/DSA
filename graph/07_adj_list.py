def add_node(v):
    if v in graph:
        print(v,"is already present in the graph!")
    else:
        graph[v] = []


def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph!")
    elif v2 not in graph:
        print(v2,"is not present in the graph!")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph!")
    else:
        graph.pop(v)
        for i in graph:
            if v in graph[i]:
                graph[i].remove(v)


def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph!")
    elif v2 not in graph:
        print(v2,"is not present in the graph!")
    else:
       graph[v1].remove(v2)
       graph[v2].remove(v1)

graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A","B")
add_edge("B","C")
add_edge("B","D")
add_edge("A","D")
print("Graph after adding edge : ",graph)


delete_node("B")
print("Graph after deleting node",graph)


delete_edge("A","D")
print("After deleting edge : ",graph)