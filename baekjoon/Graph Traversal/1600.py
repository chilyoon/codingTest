# 1600번 골드3 말이 되고픈 원숭이

'''
문제
https://www.acmicpc.net/problem/1600
입력
첫째 줄에 정수 K가 주어진다. 둘째 줄에 격자판의 가로길이 W, 세로길이 H가 주어진다. 그 다음 H줄에 걸쳐 W개의 숫자가 주어지는데, 0은 아무것도 없는 평지, 1은 장애물을 뜻한다. 장애물이 있는 곳으로는 이동할 수 없다. 시작점과 도착점은 항상 평지이다. W와 H는 1이상 200이하의 자연수이고, K는 0이상 30이하의 정수이다.

출력
첫째 줄에 원숭이의 동작수의 최솟값을 출력한다. 시작점에서 도착점까지 갈 수 없는 경우엔 -1을 출력한다.

예제 입력 1 
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
예제 출력 1 
4
예제 입력 2 
2
5 2
0 0 1 1 0
0 0 1 1 0
예제 출력 2 
-1
'''

import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
# 가로 W 세로 H
W,H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
# visit[이동수K][행H][열W]
visit = [[[-1] * W for _ in range(H)] for _ in range(K+1)]
# print(visit)
visit[K][0][0] = 0
queue = deque([(K,0,0)])

# 말의 움직임 
hx,hy = [-2,-2,-1,-1,1,1,2,2],[1,-1,2,-2,2,-2,1,-1]
# 일반 움직임
dx,dy = [-1,1,0,0],[0,0,-1,1]

while queue:
    num,x,y = queue.popleft()
    if x == W-1 and y == H-1:
        print(visit[num][y][x])
        sys.exit()
    if num > 0:
        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]
            # num-1을 비교 해야함
            if 0 <= nx < W and 0 <= ny < H and visit[num-1][ny][nx] == -1 and graph[ny][nx] == 0:
                visit[num-1][ny][nx] = visit[num][y][x] + 1
                queue.append((num-1,nx,ny))
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and visit[num][ny][nx] == -1 and graph[ny][nx] == 0:
                visit[num][ny][nx] = visit[num][y][x] + 1
                queue.append((num,nx,ny))

print(-1)