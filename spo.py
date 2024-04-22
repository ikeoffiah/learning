
#The primary goal of Depth First Search is to make sure that you have visited all the nodes of a groph
def dfs(graph, start, visited=None):
    if visited is None:

        visited = set()
    visited.add(start)
    print(visited)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Starting DFS from node 'A'
print("DFS traversal starting from 'B':")
dfs(graph, 'A')
