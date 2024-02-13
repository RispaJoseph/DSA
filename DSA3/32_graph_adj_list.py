def add_node(v):
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v]= []

def add_edge(v1,v2,w):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,w]
        list2 = [v1,w]

        graph[v1].append(list1)
        graph[v2].append(list2)


def delete_node(v):
    if v not in graph:
        print(v,"is not present in the graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)

def delete_edge(v1,v2,w):
    if v1 not in graph:
        print(v1,"is not present in graph")
    elif v2 not in graph:
        print(v2,"is not present in graph")
    else:
        list1 = [v2,w]
        list2 = [v1,w]


        if list1 in graph[v1]:
            graph[v1].remove(list1)
            graph[v2].remove(list2)
    
            



        
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
# add_node("E")

add_edge("A","B",1)
add_edge("A","D",2)
add_edge("A","C",3)
# add_edge("B","D")
print()
print(graph)
print()


# delete_node("A")


delete_edge("A","D",2)
print(graph)

# print(graph)