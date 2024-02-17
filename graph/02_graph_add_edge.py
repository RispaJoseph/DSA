def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is present in the graph!")
    else:
        node_count = node_count + 1
        nodes.append(v)

        for n in graph:
            n.append(0)

        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph!")
    elif v2 not in nodes:
        print(v2,"is not present in the graph!")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)

        graph[index1][index2] = 1
        graph[index2][index1] = 1

    



nodes = []
graph = []
node_count = 0

add_node("A")
add_node("B")
add_node("C")
add_node("D")
print(nodes)
print(graph)
print()


add_edge("A", "B")
add_edge("A", "C")
add_edge("A", "D")
print(graph)