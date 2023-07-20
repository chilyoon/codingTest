# 4963번 실버2 섬의 개수

'''
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

예제 입력 1 
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1 
0
1
1
3
1
9
'''

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

while True:
    # w 가로 h 높이
    w,h = map(int, input().split())
    if(w == 0 and h == 0):
        exit(0)
    # 섬 입력
    graph = [list(map(int, input().split())) for _ in range(h)]
    # 방문 리스트
    visit = [[-1]*w for _ in range(h)]
    # 센터 x,y (0,0) 기준 8방향 상,좌 - 하,우 +
    location = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    queue = deque()

    island = 0

    def bfs():
        global island
        while queue:
            x,y = queue.popleft()
            for i in range(8):
                nx = x + location[i][0]
                ny = y + location[i][1]
                if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1 and visit[ny][nx] == -1:
                    visit[ny][nx] = 0
                    queue.append((nx,ny))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visit[i][j] == -1:
                visit[i][j] = 0
                island += 1
                queue.append((j,i))
                bfs()

    print(island)