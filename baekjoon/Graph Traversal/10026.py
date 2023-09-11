# 10026번 골드5 적록색약

'''
문제
https://www.acmicpc.net/problem/10026
입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1 
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1 
4 3
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[ny][nx]:
                if abs(ord(color[y][x]) - ord(color[ny][nx])) == num or color[y][x] == color[ny][nx]:
                    # 방문처리 위치 조심 시간차이가 크다
                    visit[ny][nx] = True
                    queue.append((nx,ny))


N = int(input())
color = [list(map(str, input())) for _ in range(N)]
queue = deque()
# RGB 아스키 코드 82,71,66
# 적록색약 사람은 R과 G를 똑같이 본다.
# -> R = G + 11

dx,dy = [0,0,-1,1],[-1,1,0,0]
visit = [[False]*N for _ in range(N)]
cnt,cnt2 = 0,0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            visit[i][j] = True
            queue.append((j,i))
            bfs(0)
            cnt += 1

visit = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            visit[i][j] = True
            queue.append((j,i))
            bfs(11)
            cnt2 += 1
print('%d %d' % (cnt,cnt2))