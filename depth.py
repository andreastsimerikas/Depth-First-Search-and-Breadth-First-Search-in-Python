graph = {
    'A' : ['B','C'],            'N' : ['Y','Z'],      
    'B' : ['D'],                'O' : ['P','Q'],    
    'C' : ['L','M','N'],        'P' : [],
    'D' : ['E'],                'Q' : [],
    'E' : ['F','G','H','I'],    'R' : ['T'],
    'F' : [],                   'S' : ['X'],
    'G' : [],                   'T' : ['U','V','W'],
    'H' : [],                   'U' : [],
    'I' : ['J','K'],            'V' : [],
    'J' : [],                   'W' : [],
    'K' : [],                   'X' : [],
    'L' : ['O'],                'Y' : [],
    'M' : ['R','S'],            'Z' : []
}

visited = [] 

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = " ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')