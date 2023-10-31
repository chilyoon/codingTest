# 2206번 골드3 벽 부수고 이동하기

'''
문제
https://www.acmicpc.net/problem/2206
입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1
'''

import sys
from collections import deque
input = sys.stdin.readline

# (1,1) ~ (N,M) N 세로 M 가로
N,M = map(int, input().split())
# 3차원으로 벽을 한번 부쉈는지 아닌지 비교
visit = [[[-1]*(M) for _ in range(N)] for _ in range(2)]
walls = [list(map(int, input().rstrip())) for _ in range(N)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
# (0, 0)에서 시작, 벽을 부술 기회 1번
queue = deque([(1,0,0)])
visit[1][0][0] = 1

while queue:
    num, x, y = queue.popleft()
    if x == M-1 and y == N-1:
        print(visit[num][y][x])
        sys.exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if num == 1:
            # 벽을 부술 기회가 1회 남아있고 탐색하는 방향이 벽인지 확인
            if 0 <= nx < M and 0 <= ny < N and visit[num-1][ny][nx] == -1 and walls[ny][nx] == 1:
                visit[num-1][ny][nx] = visit[num][y][x] + 1
                queue.append((num-1,nx,ny))
        # 그냥 탐색
        if 0 <= nx < M and 0 <= ny < N and visit[num][ny][nx] == -1 and walls[ny][nx] == 0:
            visit[num][ny][nx] = visit[num][y][x] + 1
            queue.append((num,nx,ny))
        
print(-1)