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

def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph!")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            for j in list1:
                if v == j[0]:
                    list1.remove(j)


def delete_edge(v1,v2,w):
    if v1 not in graph:
        print(v1,"is not present in the graph!")
    elif v2 not in graph:
        print(v2,"is not present in the graph!")
    else:
        list1 = [v2,w]
        list2 = [v1,w]

        if list1 in graph[v1]:
            graph[v1].remove(list1)
            graph[v2].remove(list2)
        else:
            print("Invalid")

graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A","B",1)
add_edge("B","C",2)
add_edge("B","D",3)
add_edge("A","D",4)
print(graph)


delete_node("B")
print(graph)


delete_edge("A","D",4)
print(graph)