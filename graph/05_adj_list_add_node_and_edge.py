def add_node(v):
    if v in graph:
        print(v,"is already present in the graph!")
    else:
        graph[v] = []


def add_edge(v1,v2,w):
    if v1 not in graph:
        print(v1,"is not present in the graph!")
    elif v2 not in graph:
        print(v2,"is not present in the graph!")
    else:
        list1 = [v2,w]
        list2 = [v1,w]

        graph[v1].append(list1)
        graph[v2].append(list2)
        



graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B",1)
add_edge("A","C",2)
add_edge("B","D",1)
add_edge("D","A",1)

print(graph)
