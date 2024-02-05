# 5014번 실버1 스타트링크

'''
문제
https://www.acmicpc.net/problem/5014

입력
첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.

출력
첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.

예제 입력 1 
10 1 10 2 1
예제 출력 1 
6
예제 입력 2 
100 2 1 1 0
예제 출력 2 
use the stairs
'''

import sys
input = sys.stdin.readline
from collections import deque

# 총 f층, s 시작, g 도착, u 업, d 다운
f,s,g,u,d = map(int, input().split())

visit = [-1] * (f+1)
queue = deque([(s)])
visit[s] = 0

while queue:
    cur = queue.popleft()
    if cur == g:
        print(visit[cur])
        sys.exit()
    for i in [cur + u, cur - d]:
        if 0 < i <= f and visit[i] == -1:
            queue.append(i)
            visit[i] = visit[cur] + 1 
            # print(f'i {i} cnt {visit[i]}')

print('use the stairs')