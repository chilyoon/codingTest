# 14503번 골드5 로봇청소기

'''
문제
https://www.acmicpc.net/problem/14503

입력
첫째 줄에 방의 크기 
$N$과 
$M$이 입력된다. 
$(3 \le N, M \le 50)$  둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 
$(r, c)$와 처음에 로봇 청소기가 바라보는 방향 
$d$가 입력된다. 
$d$가 
$0$인 경우 북쪽, 
$1$인 경우 동쪽, 
$2$인 경우 남쪽, 
$3$인 경우 서쪽을 바라보고 있는 것이다.

셋째 줄부터 
$N$개의 줄에 각 장소의 상태를 나타내는 
$N \times M$개의 값이 한 줄에 
$M$개씩 입력된다. 
$i$번째 줄의 
$j$번째 값은 칸 
$(i, j)$의 상태를 나타내며, 이 값이 
$0$인 경우 
$(i, j)$가 청소되지 않은 빈 칸이고, 
$1$인 경우 
$(i, j)$에 벽이 있는 것이다. 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇 청소기가 있는 칸은 항상 빈 칸이다.

출력
로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

예제 입력 1 
3 3
1 1 0
1 1 1
1 0 1
1 1 1
예제 출력 1 
1
예제 입력 2 
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
예제 출력 2 
57

구현문제인데 BFS로 풂
'''

import sys
input = sys.stdin.readline
from collections import deque

# m x n
n,m = map(int, input().split())

# 현재좌표 x,y 0 북 1 동 2 남 3 서
Y,X,location = map(int, input().split())
queue = deque([(X,Y,location)])

room = [list(map(int, input().split())) for _ in range(n)]

visit = [[False] * m for _ in range(n)]
visit[Y][X] = True

# 북 동 남 서
dx, dy = [0,1,0,-1], [-1,0,1,0]

cnt = 1
while queue:
    x,y,l = queue.popleft()
    # print(f'x {x} y {y} l {l}')
    flag = True
    for i in range(1,5):
        loc = (l-i)%4
        nx = x + dx[loc]
        ny = y + dy[loc]
        if 0 <= nx < m and 0 <= ny < n and room[ny][nx] == 0 and not visit[ny][nx]:
            # print(f' nx {nx} ny {ny} loc {loc} room {room[ny][nx]}')
            flag = False
            visit[ny][nx] = True
            cnt += 1
            queue.append((nx,ny,loc))
            break
    # 청소되지 않은 빈 칸이 없는 경우
    if flag:
        nx = x + (-dx[l])
        ny = y + (-dy[l])
        if 0 <= nx < m and 0 <= ny < n:
            if room[ny][nx] == 0:
                queue.append((nx,ny,l))
                # print(f'back {nx} {ny}')
            else:
                break

# print(*visit,sep='\n')
print(cnt)