V = int(input("Enter number of Vertex:")) # no of vertex
E = int(input("Enter number of Edges:"))   # No of egdes

adj = [[0]*V for _ in range(V)] # V x V matrix



# Mention the starting vertex


def helper(adj,sv,visited):
    num_vertex = len(adj)
    visited[sv] = True
    for i in range(num_vertex): # go to every vertex
        if adj[sv][i] == 1 and visited[i] is False:
            #print(i)
            dfs(adj,i,visited)

def print_graph(adj):
    visited = [False]* (len(adj))

    for i in range(len(adj)):
        if visited[i] == False:
            
            dfs(adj,i,visited)




for _ in range(E):

    sv = int(input("Enter starting vertex: "))
    ev = int(input("Enter ending vertex: "))

    # for undirected graph
    adj[sv][ev] = 1
    adj[ev][sv] = 1

for items in adj:
    print(items , end ="\n")
print(print_graph(adj))
