# 18404번 실버1 현명한 나이트

'''
문제
https://www.acmicpc.net/problem/18404

입력
첫째 줄에 N과 M이 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ N ≤ 500, 1 ≤ M ≤ 1,000) 둘째 줄에 나이트의 위치 (X, Y)를 의미하는 X와 Y가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ X, Y ≤ N) 셋째 줄부터 M개의 줄에 걸쳐 각 상대편 말의 위치 (A, B)를 의미하는 A와 B가 공백을 기준으로 구분되어 자연수로 주어진다. (1 ≤ A, B ≤ N)

단, 입력으로 주어지는 모든 말들의 위치는 중복되지 않으며, 나이트가 도달할 수 있는 위치로만 주어진다.

출력
첫째 줄에 각 상대편 말을 잡기 위한 최소 이동 수를 공백을 기준으로 구분하여 출력한다.

단, 출력할 때는 입력 시에 상대편 말 정보가 주어졌던 순서에 맞게 차례대로 출력한다.

예제 입력 1 
5 3
2 4
3 2
3 5
4 5
예제 출력 1 
1 2 1
'''

import sys
from collections import deque
input = sys.stdin.readline

# N x N 체스판 M개의 상대편 말
N,M = map(int, input().split())

# 0은 빈판 1은 나이트 2는 상대편 말
chess = [[0]*(N+1) for _ in range(N+1)]
visit = [[-1]*(N+1) for _ in range(N+1)]

# 나이트의 위치 (X,Y)
X,Y = map(int, input().split())
chess[X][Y] = 1
visit[X][Y] = 0
queue = deque([(X,Y)])

# 나이트의 이동 가능한 위치
dx,dy = [-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]

enemy = deque()
for _ in range(M):
    x,y = map(int, input().split())
    enemy.append((x,y))
    chess[x][y] = 2

#print(*chess, sep='\n')

while queue:
    x,y = queue.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N and 0 <= ny <= N and visit[nx][ny] == -1:
            visit[nx][ny] = visit[x][y] + 1
            queue.append((nx,ny))

for x,y in enemy:
    print(visit[x][y], end=' ')