# Method 1 using Parents:
---------------------------


adj = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def backtrace(parent,start,end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

# {'2': '1', '3': '1', '4': '1', '5': '2', '6': '2', '7': '4', '8': '4', '9': '5', '10': '5', '11': '7', '12': '7'}

def bfs(adj,start,end):
    parent = {}
    queue = [start]

    while queue:
        front = queue.pop(0)

        if front == end:
            return backtrace(parent,start,end)

        for i in adj.get(front,[]):
            if i not in queue:
                parent[i] = front
                queue.append(i)
                
print(bfs(adj, '1', '11'))


# Method 2:
------------

graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [10],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}


def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.add(vertex)


print bfs(graph, 1, 13)

# Method 3 without using get:
#-------------------------------

graph = {
         'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
         }
def retunShortestPath(graph, start, end):

    queue = [(start,[start])]
    visited = set()

    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)
        for node in graph[vertex]:
            if node == end:
                return path + [end]
            else:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))

