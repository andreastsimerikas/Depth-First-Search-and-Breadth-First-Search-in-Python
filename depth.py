import time
start_time = time.perf_counter()

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

def dfs(visited, graph, node, target):
    if node not in visited:
        time.sleep(0.1)
        print(node, end = " ")
        visited.append(node)
        if node == target:
            print('/n')
            print(time.perf_counter() - start_time)

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, target)

dfs(visited, graph, 'A', 'X')


