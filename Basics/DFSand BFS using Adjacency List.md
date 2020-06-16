<b>DFS:</b>

<pre>
<b>The Algorithm</b>
Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
Repeat until all the nodes are visited, or the node to be searched is found.
</pre>

<pre>Adjacency list can be given in two ways:

1- List of List like:   [[1],[0,3],[5],[1,2,3]]:
                        
                        In such cases the index if the vertex of the graph

2- In the form of hashmap like: graph = {
                                            'A' : ['B','C'],
                                            'B' : ['D', 'E'],
                                            'C' : ['F'],
                                            'D' : [],
                                            'E' : ['F'],
                                            'F' : []
                                        }
                                        
                         In these cases key = Vertex and it's value represent the neighbours of that vertex

Code:
______

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')

</pre>

<b>BFS</b>

<pre>
<b>The Algorithm</b>
Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
If there are no remaining adjacent vertices left, remove the first vertex from the queue.
Repeat step 1 and step 2 until the queue is empty or the desired node is found.
</pre>
<pre>

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')
</pre>
