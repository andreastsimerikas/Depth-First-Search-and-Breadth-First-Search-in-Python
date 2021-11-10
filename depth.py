graph = {
    'A' : ['B','C','D'],
    'B' : ['H'],
    'C' : ['E','F'],
    'D' : ['G','I'],
    'E' : ['F'],
    'F' : ['H','I'],
    'G' : [],
    'H' : [],
    'I' : []
}

visited = [] 

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')