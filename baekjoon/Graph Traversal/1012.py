# 1012번 실버2 유기농 배추

'''
문제
https://www.acmicpc.net/problem/1012
입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

예제 입력 1 
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
예제 출력 1 
5
1
예제 입력 2 
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
예제 출력 2 
2
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):
    # print('x %d y %d' % (x,y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and (nx,ny) not in visit:
            visit[(nx,ny)] = visit[(x,y)] + 1
            dfs(nx,ny)

dx,dy = [-1,1,0,0],[0,0,-1,1]

T = int(input())
for _ in range(T):
    # M 가로 N 세로 K 배추 개수
    M,N,K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    visit = {}
    napa = []
    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1
        napa.append((x,y))
    # print(napa)
    earthworm = 0
    for i in napa:
        if i not in visit:
            visit[i] = 0
            earthworm += 1
            dfs(i[0],i[1])
    print(earthworm)