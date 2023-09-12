# 16948번 실버1 데스나이트

'''
문제
https://www.acmicpc.net/problem/16948
입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

예제 입력 1 
7
6 6 0 1
예제 출력 1 
4
예제 입력 2 
6
5 1 0 5
예제 출력 2 
-1
예제 입력 3 
7
0 3 4 3
예제 출력 3 
2
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
# row 열 col 행
r1,c1,r2,c2 = map(int, input().split())
visit = [[-1]*N for _ in range(N)]
visit[r1][c1] = 0
dr,dc = [-2,-2,0,0,2,2],[-1,1,-2,2,-1,1]
queue = deque([(r1,c1)])

while queue:
    r,c = queue.popleft()
    if r == r2 and c == c2:
        print(visit[r][c])
        sys.exit()
    for i in range(6):
       nr = r + dr[i]
       nc = c + dc[i]
       if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == -1:
           visit[nr][nc] = visit[r][c] + 1
           queue.append((nr,nc)) 

print(-1)