def bfs_shortest_distance(start_node, end_node, graph):
    visited = set()
    distance = {start_node: 0}
    
    if start_node not in graph or end_node not in graph:
        print("Start or end node not present in the graph.")
        return -1  # Indicate failure
    

    import collections
    queue = collections.deque([start_node])
    
    while queue:
        current = queue.popleft()
        visited.add(current)
        
        for i in graph[current]:
            if i not in visited:
                queue.append(i)
                distance[i] = distance[current] + 1
                
                if i == end_node:
                    return distance[i]
    
    print("End node is not reachable from the start node.")
    return -1  # Indicate failure

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_node = 'A'
end_node = 'C'

result = bfs_shortest_distance(start_node,end_node,graph)
print(result)