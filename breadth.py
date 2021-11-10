graph = {
    'A' : ['B','C','D'],
    'B' : ['A','H'],
    'C' : ['A','E','F'],
    'D' : ['A','G','I'],
    'E' : ['C','F'],
    'F' : ['C','E','H','I'],
    'G' : ['D'],
    'H' : ['F','B'],
    'I' : ['F','D']
}

visited = []  
queue = []    

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print(s) 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, 'A')