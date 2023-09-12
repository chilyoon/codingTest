# 16973번 골드4 직사각형 탈출

'''
문제
https://www.acmicpc.net/problem/16973
입력
첫째 줄에 격자판의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에 격자판의 각 칸의 정보가 주어진다. 0은 빈 칸, 1은 벽이다.

마지막 줄에는 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc가 주어진다.

격자판의 좌표는 (r, c) 형태이고, r은 행, c는 열이다. 1 ≤ r ≤ N, 1 ≤ c ≤ M을 만족한다.

출력
첫째 줄에 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

제한
2 ≤ N, M ≤ 1,000
1 ≤ H ≤ N
1 ≤ W ≤ M
1 ≤ Sr ≤ N-H+1
1 ≤ Sc ≤ M-W+1
1 ≤ Fr ≤ N-H+1
1 ≤ Fc ≤ M-W+1
입력으로 주어진 직사각형은 격자판을 벗어나지 않고, 직사각형이 놓여 있는 칸에는 벽이 없다.
예제 입력 1 
4 5
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
2 2 1 1 1 4
예제 출력 1 
7
아래, 아래, 오른쪽, 오른쪽, 오른쪽, 위, 위

예제 입력 2 
6 7
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
0 0 0 0 0 0 0
2 3 1 1 5 5
예제 출력 2 
8
아래, 아래, 오른쪽, 오른쪽, 오른쪽, 아래, 아래, 오른쪽
'''

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
# 0 빈칸 1 벽
rect = [list(map(int, input().split())) for _ in range(N)]
# 벽 저장 -> 시간단축
# 사각형을 하나하나 옮겨서 벽검사 X
# 사각형을 옮긴후 그 안에 벽이 있는지 검사
walls = []
for i in range(N):
    for j in range(M):
        if rect[i][j] == 1:
            walls.append((j,i))
# 체크 함수
def check(j,i):
    for c,r in walls:
        if i <= r < i+H and j <= c < j+W:
            return False
    return True
visit = [[-1]*M for _ in range(N)]
# 직사각형의 크기 H(y),W(x) 시작좌표 Sr,Sc 도착 좌표 Fr,Fc
# 좌표는 직사각형의 가장 왼쪽 위
# 1 <= r <= N 행(y) 1 <= c <= M 열(x)
H,W,Sr,Sc,Fr,Fc = map(int, input().split())
visit[Sr-1][Sc-1] = 0
queue = deque([(Sc-1,Sr-1)])

dx,dy = [-1,1,0,0],[0,0,-1,1]
while queue:
    x,y = queue.popleft()
    if x == Fc-1 and y == Fr-1:
        print(visit[y][x])
        sys.exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nx+W-1 < M and 0 <= ny+H-1 < N:
            if visit[ny][nx] == -1:
                if check(nx,ny):
                    visit[ny][nx] = visit[y][x] + 1
                    queue.append((nx,ny))
print(-1)