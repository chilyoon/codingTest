# 18232번 실버2 텔로포트 정거장

'''
문제
https://www.acmicpc.net/problem/18232

입력
첫 번째 줄에 정수 N, M이 공백으로 구분되어 주어진다. (2 ≤ N ≤ 300,000, 0 ≤ M ≤ min(N×(N-1)/2, 300,000))

두 번째 줄에 정수 S, E가 공백으로 구분되어 주어진다. (1 ≤ S, E ≤ N, S ≠ E)

그 다음 줄부터 M개의 줄에 걸쳐 텔레포트 연결 정보를 의미하는 정수 x, y가 주어진다. (1 ≤ x, y ≤ N, x ≠ y)

x y는 점 x의 텔레포트와 점 y의 텔레포트가 연결되어 있다는 뜻이다. M개의 연결정보는 중복되는 x y쌍이 없도록 주어진다.

출력
첫 번째 줄에 주예와 방주가 만날 수 있는 최소 시간을 출력한다.

예제 입력 1 
5 1
1 5
1 4
예제 출력 1 
2
예제 입력 2 
10 3
2 5
1 6
1 3
2 8
예제 출력 2 
3
'''

import sys
input = sys.stdin.readline
from collections import deque

# 1~n m번
n,m = map(int, input().split())
# 주예 s 방주 e
s,e = map(int, input().split())
# x,y가 m번
tel = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    tel[x].append(y)
    tel[y].append(x)

visit = [-1] * (n+1)
visit[s] = 0
queue = deque([(s)])

while queue:
    x = queue.popleft()
    # print(f'x = {x}')
    if x == e:
        print(visit[x])
        break
    for i in [x-1,x+1]:
        if 0 <= i <= n and visit[i] == -1:
            visit[i] = visit[x] + 1
            queue.append(i)
    for i in tel[x]:
        if visit[i] == -1:
            visit[i] = visit[x] + 1
            queue.append(i)