# 17142번 골드3 연구소 3

'''
문제
https://www.acmicpc.net/problem/17142

입력
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.

둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

출력
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
예제 출력 1 
4
예제 입력 2 
7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 2 
4
예제 입력 3 
7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 3 
4
예제 입력 4 
7 5
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 4 
3
예제 입력 5 
7 3
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 5 
7
예제 입력 6 
7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
예제 출력 6 
-1
예제 입력 7 
5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1
예제 출력 7 
0

--> 비활성화 된 바이러스를 사방탐색하는 방식은 0 * * * 0 이 되어버리면
    반례가 발생 빈 벽을 지나갈때만 time을 비교하는 방식으로 진행 해야한다
'''

import sys
import copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def bfs(visi, position):
    time = 0
    queue = deque()
    visit = copy.deepcopy(visi)
    for x,y in position:
        visit[y][x] = 0
        queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[ny][nx] != '-':
                if visit[ny][nx] == -1:
                    visit[ny][nx] = visit[y][x] + 1
                    time = max(time, visit[ny][nx])
                    queue.append((nx,ny))
                elif visit[ny][nx] == '*':
                    visit[ny][nx] = visit[y][x] + 1
                    queue.append((nx,ny))

    for i in range(n):
        for j in range(n):
            if visit[i][j] == -1:
                return -1   
        
    return time

# n x n 연구소, m개 바이러스
n,m = map(int, input().split())
lab = []
virus = []
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        # 0은 빈칸 1은 벽 2는 바이러스
        if l[j] == 1:
            l[j] = '-'
        elif l[j] == 2:
            # (x,y)
            virus.append((j,i))
            l[j] = '*'
        else:
            l[j] = -1
    lab += [l]

dx,dy = [0,0,-1,1],[-1,1,0,0]

s = 5000
for position in combinations(virus,m):
    result = bfs(lab, position)
    if 0 <= result < s:
        s = result

print(s if s != 5000 else -1)