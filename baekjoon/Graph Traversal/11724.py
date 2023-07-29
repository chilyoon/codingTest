# 11724번 실버2 연결 요소의 개수

'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
예제 입력 2 
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2 
1
'''

import sys
input = sys.stdin.readline
# 최대 재귀 깊이 변경
sys.setrecursionlimit(10**6)

# 정점 N 간선 M
N,M = map(int, input().split())
graph = [[-1]*(N+1) for _ in range(N+1)]
visit = [False]*(N+1)
for _ in range(M):
    u,v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(V):
    visit[V] = True
    for i in range(1,N+1):
        if not visit[i] and graph[V][i] == 1:
            dfs(i)

cnt = 0
for i in range(1,N+1):
    if not visit[i]:
        cnt += 1
        dfs(i)

print(cnt)