import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# root는 1
N = int(input()) # 노드 개수 N

graph = [[] for _ in range(N+1)]
parent = [0]*(N+1)
dfs_g = [False] * (N+1)

for i in range(N-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(V):
    dfs_g[V] = True
    #for i in range(1,N+1):
        #if not parent[V] and dfs_g[V] and graph[V][i] == 1:
            #parent[V] = [V,i]
    for i in graph[V]:    
        if not dfs_g[i]:
            parent[i] = V
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(parent[i])