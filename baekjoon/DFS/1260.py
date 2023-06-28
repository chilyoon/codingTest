# 실버2 1260번 DFS와 BFS

'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999
'''

from collections import deque

# 정점 N 간선 M 시작번호 V
N,M,V = map(int, input().split())

# 초기화, N+1을 시작하여 0번 인덱스를 버림
graph = [[0] * (N+1) for _ in range(N+1)]
dfs_g = [False] * (N+1)
# dfs_g = [False, False, False...] 0 빼고 1부터 N+1까지 총 N개
bfs_g = [False] * (N+1)

# 간선 양방향 구현 연결o 1 연결x 0
# x->y, y->x 
for _ in range(M):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# DFS 깊이우선탐색
def dfs(V):
    dfs_g[V] = True # V번에 방문했으니 True
    print(V, end=' ')
    for i in range(1, N+1):
        # dfs_g가 False이고(not dfs_g[i]) 간선이 연결되어 있다면
        # i 값으로 다시 재귀함수
        if not dfs_g[i] and graph[V][i] == 1:
            dfs(i)

# BFS 넓이우선탐색
def bfs(V):
    bfs_g[V] = True
    # deque 사용 queue = deque([])
    queue = deque()
    # V를 queue에 넣음
    queue.append(V)
    while queue:
        popV = queue.popleft()
        print(popV, end=' ')
        for i in range(1, N+1):
            # bfs_g[i]가 False이고 간설이 연결되어 있다면
            # queue에 i를 넣고 bfs_g[i]도 방문했으니 True
            if not bfs_g[i] and graph[popV][i] == 1:
                queue.append(i)
                bfs_g[i] = True

dfs(V)
print()
bfs(V)