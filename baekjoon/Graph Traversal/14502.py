# 14502번 골드4 연구소

'''
문제
https://www.acmicpc.net/problem/14502

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

예제 입력 1 
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1 
27
예제 입력 2 
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력 2 
9
예제 입력 3 
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 3 
3
'''

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
from copy import deepcopy

def bfs(lab, position):
    visit = deepcopy(lab)
    sQ = deepcopy(queue)

    for x,y in position:
        visit[y][x] = 1

    while sQ:
        x,y = sQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[ny][nx] == 0:
                visit[ny][nx] = 2
                sQ.append((nx,ny))
    
    r = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0:
                r += 1
    
    return r

# 세로n 가로 m
n,m = map(int, input().split())
lab = []
empty = []
queue = deque()
dx,dy = [0,0,-1,1],[-1,1,0,0]

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(m):
        if l[j] == 2:
            queue.append((j,i))
        elif l[j] == 0:
            empty.append((j,i))
    lab += [l]

answer = 0
for position in combinations(empty, 3):
    result = bfs(lab, position)
    if result > answer:
        answer = result

print(answer)