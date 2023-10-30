# 16928번 골드5 뱀과 사다리 게임

'''
문제
https://www.acmicpc.net/problem/16928
입력
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다. x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다. u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 항상 100번 칸에 도착할 수 있는 입력만 주어진다.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.

예제 입력 1 
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
예제 출력 1 
3
5를 굴려 6으로 이동한다.
6을 굴려 12로 이동한다. 이 곳은 98로 이동하는 사다리가 있기 때문에, 98로 이동한다.
2를 굴려 100으로 이동한다.
예제 입력 2 
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
예제 출력 2 
5
5를 굴려 6으로 이동하고, 사다리를 이용해 80으로 이동한다. 
6을 굴려 86으로
6을 또 굴려 92로
6을 또 굴려 98로 이동하고
2를 굴려 100으로 이동한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

# 사다리의 수 N 뱀의 수 M
N,M = map(int, input().split())

ladder_snake = dict()
for _ in range(N):
    # x번 -> y번 사다리 이동 높아지는거
    x,y = map(int, input().split())
    ladder_snake[x] = y

for _ in range(M):
    # u번 -> v번 뱀 이동 낮아지는거
    u,v = map(int, input().split())
    ladder_snake[u] = v

# 1번 ~ 100번
visit = [0] * 101

queue = deque([1])

while queue:
    cur = queue.popleft()
    if cur == 100:
        print(visit[cur])
        sys.exit()
    for i in range(1,7):
        next = cur + i
        if next <= 100 and visit[next] == 0:
            if next in ladder_snake.keys():
                if visit[ladder_snake.get(next)] == 0:
                    visit[next] = visit[cur] + 1
                    visit[ladder_snake.get(next)] = visit[next]
                    queue.append(ladder_snake.get(next))
                else:
                    continue
            else:
                visit[next] = visit[cur] + 1
                queue.append(next)