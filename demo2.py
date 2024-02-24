def add_node(v):
    global node_count
    if v in graph:
        print("{v} is not present in the graph")
    else:
        nodes.append(v)
        node_count = node_count + 1

        for n in graph:
            n.append(0)

        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,w):
    if v1 not in nodes:
        print(f"{v1} not present in the graph")

    elif v2 not in nodes:
        print(f"{v2} not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = w
        graph[index2][index1] = w

def delete_node(v):
    if v not in nodes:
        print(f"{v} not in present in the graph")
    else:
        index1 = nodes.index(v)
        nodes.pop(index1)

        graph.pop(index1)
        for i in graph:
            i.pop(index1)

def delete_edge(v1,v2):
    if v1 not in nodes:
        print(f"{v1} not present in the graph!")
    elif v2 not in nodes:
        print(f"{v2} not present in the graph!")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = 0
        graph[index2][index1] = 0




            

node_count = 0
nodes = []
graph = []

add_node("A")
add_node("B")
add_node("C")

add_edge("A","B",1)
add_edge("B","C",2)


delete_node("C")

delete_edge("A","B")

print(nodes)
print(graph)