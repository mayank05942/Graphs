# Concept: https://www.youtube.com/watch?v=0XYSdIVY6Ks
#          https://www.youtube.com/watch?v=3kkiRfMWBIc&list=PLpO3gASfJEIJ6cYs4kAY3SnH2kpohSTZI&index=5&t=0s


# In DFS once we start exploring an vertex we keep exploring it until we cannot got further
# once we cannot go further using visited array we backtrack and then explore the other possiblilty

# To understand that watch last part of first video.

# Time complexity: O(V+E)  V because we have to visit all vertex and E because we have to backtrack also.
# Space: O(V)

_____________________________________________________________________________________________________________________________________

V = int(input("Enter number of Vertex:")) # no of vertex
E = int(input("Enter number of Edges:"))   # No of egdes

adj = [[0]*V for _ in range(V)]        # V x V matrix


def dfs(adj,sv,visited):
    print(sv)
    num_vertex = len(adj)
    visited[sv] = True
    for i in range(num_vertex): # go to every vertex
        if adj[sv][i] == 1:
        
            if visited[i] is True:  # if we have already visited then leave it check other options
                continue

            dfs(adj,i,visited)

def print_graph(adj):

    visited = [False]* (len(adj))

    for i in range(len(adj)):
        if visited[i] == False:  # explore only that part which is not visited otherwise we will run in an infinite cycle
            dfs(adj,i,visited)   # recursion

# Taking input of the graph:

for _ in range(E):

    sv = int(input("Enter starting vertex: "))
    ev = int(input("Enter ending vertex: "))

    # for undirected graph
    adj[sv][ev] = 1
    adj[ev][sv] = 1
    
 # At the end of the for loop we will have the adjacency matrix

for items in adj:
    print(items , end ="\n")
    
print_graph(adj)
