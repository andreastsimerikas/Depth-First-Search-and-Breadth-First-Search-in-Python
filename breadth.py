graph = {
    'A' : ['B','C','D'],
    'B' : ['G'],
    'C' : ['E','F'],
    'D' : ['G','I'],
    'E' : [],
    'F' : ['H','I'],
    'G' : [],
    'H' : [],
    'I' : []
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