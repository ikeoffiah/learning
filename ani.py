def bsf(graph, start, visited=[]):
    if start not in visited:
        visited.append(start)

    start_children = graph[start]
    formated_children = []
    for i in start_children:
        if i not in visited:
            visited.append(i)
            formated_children.append(i) #add children that haven't been visited
    if formated_children !=[]: # iterate over unvisited children
        for i in formated_children:
            if i in visited:
                bsf(graph, i, visited)

    return visited



def dsf(graph, start, visited=[]):

    if start not in visited:
        visited.append(start)

    for i in graph[start]:
        if i not in visited:
            dsf(graph, i, visited)
    return visited


def bsf2(graph,start):

    queue = [start]
    visted = []

    while queue !=[]:

        node = queue.pop(0)
        visted.append(node)

        children = graph[node]

        for i in children:
            if i not in visted:

                queue.append(i)



    return visted

# def dsf2(graph, start):





graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G', 'H'],
    'F': ['C', 'I'],
    'G': ['E'],
    'H': ['E'],
    'I': ['F']
}



print("BFS traversal starting from node A:")
print(bsf2(graph, 'A'))
# print(dsf(graph, 'A'))