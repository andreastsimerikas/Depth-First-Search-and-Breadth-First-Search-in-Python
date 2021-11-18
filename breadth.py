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
queue = []    

def bfs(visited, graph, node, target):
  visited.append(node)
  queue.append(node)

  while queue:
    time.sleep(0.1)
    s = queue.pop(0) 
    print(s, end = " ") 

    if s == target:
      print('/n')
      print(time.perf_counter() - start_time)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, 'A', 'X')