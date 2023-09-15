# 2573번 골드4 빙산

'''
문제
https://www.acmicpc.net/problem/2573
입력
첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는 M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다. 배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

출력
첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

예제 입력 1 
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
예제 출력 1 
2

예제 입력 2
5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
예제 출력 2
0
-> 빙산이 다 녹으면 0 출력
예제 입력 3
5 5
0 0 0 0 0
0 0 9 0 0
0 0 3 1 0
0 0 9 0 0
0 0 0 0 0
예제 출력 3
2
-> 녹은 빙산 값이 -가 되지 않도록 처리
'''

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            cnt = 0
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위내에 있고 0일시 cnt증가 0이 아니면 큐에 추가
            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx]:
                if iceberg[ny][nx] == 0:
                    cnt += 1
                elif iceberg[ny][nx] > 0:
                    visit[ny][nx] = True
                    queue.append((nx,ny))
            if iceberg[y][x] - cnt >= 0:
                iceberg[y][x] -= cnt
            else:
                iceberg[y][x] = 0

year = 0
# 1년당 queue, visit 초기화
while(True):
    island = 0
    queue = deque()
    visit = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and not visit[i][j]:
                # print('i %d j %d' %(i,j))
                visit[i][j] = True
                queue.append((j,i))
                bfs()
                island += 1
                if island > 1:
                    print(year)
                    sys.exit()
    # print(*iceberg, sep='\n')
    # print()
    
    if island == 0:
        print(0)
        sys.exit()
    else:
        year += 1
    