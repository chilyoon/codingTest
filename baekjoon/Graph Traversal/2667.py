# 2667번 실버1 단지번호 붙이기

'''
문제
<그림 1>과 같이 정사각형 모양의 지도가 있다. 
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1 
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
예제 출력 1 
3
7
8
9
'''

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
visit = [[-1]*N for _ in range(N)]
danji = []
queue = deque()

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and visit[nx][ny] == -1:
                visit[nx][ny] = 0
                cnt += 1
                queue.append((nx,ny))
    danji.append(cnt)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == -1:
            queue.append((i,j))
            visit[i][j] = 0
            bfs()

danji.sort(key = lambda x: x)
print(len(danji))

for i in range(len(danji)):
    print(danji[i])