# 4179번 골드4 불!

'''
문제
https://www.acmicpc.net/problem/4179

입력
입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

각각의 문자들은 다음을 뜻한다.

#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
F: 불이 난 공간
J는 입력에서 하나만 주어진다.

출력
지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.

예제 입력 1 
4 4
####
#JF#
#..#
#..#
예제 출력 1 
3
반례

3 4
##.#
FJ.#
##F#

ans : IMPOSSIBLE	

5 5
FFFFF
..J..
.....
.....
.....

answer:4	

4 4
####
#J##
##F.
##.#

IMPOSSIBLE	

4 4
####
#JF#
#..#
#..F

IMPOSSIBLE
4 4
#F##
#F##
..J#
####

IMPOSSIBLE	

5 5
#F..#
#.J.#
###.#
###.#
###.#

5	

5 5
#####
#F#J#
###.#
###.#
###.#

4	

2 2
JF
FF

1

4 102
######################################################################################################
#J....................................................................................................
#F....................................................................................................
######################################################################################################

101
'''

import sys
from collections import deque
input = sys.stdin.readline

# R 세로 C 가로
R,C = map(int, input().split())
queue = deque()
visit = [[-1]*C for _ in range(R)]
maze = []
for i in range(R):
    maze.append(list(map(str, input())))
    # 미로를 확인해 벽(#)은 -2 불(F)은 -3 지훈(J)은 0으로 visit에 처리
    for j in range(C):
        chk = maze[i][j]
        if chk == '#':
            visit[i][j] = -2
        elif chk == 'J':
            visit[i][j] = 1
            queue.append((j,i))
        elif chk == 'F':
            visit[i][j] = -3
            queue.appendleft((j,i))
        

dx,dy = [0,0,-1,1], [-1,1,0,0]
while queue:
    x,y = queue.popleft()
    if not(0 < y < R-1 and 0 < x < C-1) and visit[y][x] == 1 :
        print(1)
        sys.exit()
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R:
                if visit[y][x] >= 0 and visit[ny][nx] == -1:
                    if 0 < ny < R-1 and 0 < nx < C-1:
                        visit[ny][nx] = visit[y][x] + 1
                        queue.append((nx,ny))
                    else:
                        visit[ny][nx] = visit[y][x] + 1
                        print(visit[ny][nx])
                        sys.exit()
                elif visit[y][x] == -3 and visit[ny][nx] == -1:
                    visit[ny][nx] = -3
                    queue.append((nx,ny))

print('IMPOSSIBLE')
