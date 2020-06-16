<b>DFS:</b>

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
