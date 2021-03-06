
# Explanation: https://www.youtube.com/watch?v=6Fw4jYtP6jU&list=PLpO3gASfJEIJ6cYs4kAY3SnH2kpohSTZI&index=6&t=0s

# Time: O(V+E) since we are visiting and then removing from queue both will take time # no of times we visit the vertex
# No backtracking here since we don't use recursion here.
# we use queue to visit all adjacent nodes.
# Space: O(V)

#_______________________________________________________________________________________________________________________________________


V = int(input("Enter number of Vertex:")) # no of vertex
E = int(input("Enter number of Edges:"))   # No of egdes

adj = [[0]*V for _ in range(V)] # V x V matrix
# Mention the starting vertex
def bfs(adj,sv,visited):
    queue = [sv]

    num_vertex = len(adj)
    visited[sv] = True
    while queue:
        front = queue.pop(0)
        print(front)
        # now we have to check what are the edges that are connected with this vertex
        # for that we will use for loop to check all connections
        for i in range(num_vertex):
            if adj[front][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True

def print_graph(adj):

    visited = [False]* (len(adj))

    for i in range(len(adj)):
        if visited[i] == False:

            bfs(adj,i,visited)

for _ in range(E):

    sv = int(input("Enter starting vertex: "))
    ev = int(input("Enter ending vertex: "))

    # for undirected graph
    adj[sv][ev] = 1
    adj[ev][sv] = 1

for items in adj:
    print(items , end ="\n")

print_graph(adj)
