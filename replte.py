


def dfs(graph, start, main_arrangement = []):

    if start not in main_arrangement:
        main_arrangement.append(start)



    for i in graph[start]:
        if i not in main_arrangement:
            dfs(graph, i, main_arrangement)
    return main_arrangement






graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

# Starting DFS from node 'A'
print("DFS traversal starting from 'B':")
dfs(graph, 'A')

print(dfs(graph, 'A'))
# ['A', 'B', 'D', 'E', 'F', 'C']