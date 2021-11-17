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
queue = []    

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print(s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, 'A')