# 3184번 실버1 양

'''
문제
https://www.acmicpc.net/problem/3184

입력
첫 줄에는 두 정수 R과 C가 주어지며(3 ≤ R, C ≤ 250), 각 수는 마당의 행과 열의 수를 의미한다.

다음 R개의 줄은 C개의 글자를 가진다. 이들은 마당의 구조(울타리, 양, 늑대의 위치)를 의미한다.

출력
하나의 줄에 아침까지 살아있는 양과 늑대의 수를 의미하는 두 정수를 출력한다.

예제 입력 1 
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###
예제 출력 1 
0 2
예제 입력 2 
8 8
.######.
#..o...#
#.####.#
#.#v.#.#
#.#.o#o#
#o.##..#
#.v..v.#
.######.
예제 출력 2 
3 1
예제 입력 3 
9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
예제 출력 3 
3 5

'''

import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs():
    sheep, wolf = 0,0
    while queue:
        x,y = queue.popleft()
        if field[y][x] == 'o':
            sheep += 1
        elif field[y][x] == 'v':
            wolf += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r and not visit[ny][nx] and field[ny][nx] != '#':
                visit[ny][nx] = True
                queue.append((nx,ny))
    # print(f'sheep {sheep} wolf {wolf}')
    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return [sheep,wolf]

# 마당 행r 열c
r,c = map(int, input().split())
field = [list(input()) for _ in range(r)]

visit = [[False]*c for _ in range(r)]
queue = deque()

answer = [0,0]
for i in range(r):
    for j in range(c):
        if not visit[i][j] and field[i][j] != '#':
            visit[i][j] = True
            queue.append((j,i))
            s,e = bfs()
            # print(f'양 {s} 늑대 {e}')
            answer[0] += s
            answer[1] += e

print(*answer)