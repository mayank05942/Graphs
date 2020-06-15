#Concept: https://www.youtube.com/watch?v=0XYSdIVY6Ks
#          https://www.youtube.com/watch?v=3kkiRfMWBIc&list=PLpO3gASfJEIJ6cYs4kAY3SnH2kpohSTZI&index=5&t=0s


V = int(input("Enter number of Vertex:")) # no of vertex
E = int(input("Enter number of Edges:"))   # No of egdes

adj = [[0]*V for _ in range(V)] # V x V matrix
# Mention the starting vertex
def dfs(adj,sv,visited):
    print(sv)
    num_vertex = len(adj)
    visited[sv] = True
    for i in range(num_vertex): # go to every vertex
        if adj[sv][i] == 1:
            if visited[i] is True:
                continue

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
