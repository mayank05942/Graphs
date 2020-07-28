#adj = [[1,0],[2,0],[3,1],[3,2]]



ans = []
stack = []
visited = [False]*len(adj)

def dfs(sv,visited,adj,stack):
    for i in adj[sv]:
        if visited[i] == False:
            visited[i] = True
            dfs(i,visited,adj,stack)

    stack.append(sv)



for sv in range(len(visited)):
    if visited[sv] == False:
        visited[sv] = True
        dfs(sv,visited,adj,stack)

while stack:
    ans.append(stack.pop())

print(ans)
