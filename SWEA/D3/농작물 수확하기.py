# 2805. 농작물 수확하기 D3

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

[제약 사항]

농장의 크기 N은 1 이상 49 이하의 홀수이다. (1 ≤ N ≤ 49)

농작물의 가치는 0~5이다.

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 농장의 크기 N과 농장 내 농작물의 가치가 주어진다.

[출력]

각 줄은 '#t'로 시작하고, 공백으로 농장의 규칙에 따라 얻을 수 있는 수익을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
2
5
14054
44250
02032
51204
52212
7
0001000
0011100
0111110
1111111
0111110
0011100
0001000

출력
#1 23
#2 25

'''

import sys
sys.stdin = open("../input.txt", "r")

from collections import deque

T = int(input())

for t in range(1,T+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]
    visit = [[False]*N for _ in range(N)]

    center = N // 2
    result = field[center][center]
    visit[center][center] = True

    dx,dy = [-1,1,0,0],[0,0,-1,1]

    queue = deque([(center,center)])
    if center > 0:
        while queue:
            x,y = queue.popleft()
            # 벽에 마주했을때 탐색해야하는 범위가 끝났으니 break
            if y == center and x == 0:
                break
            # print(f'x{x} y{y}')
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visit[ny][nx]:
                    queue.append((nx,ny))
                    result += field[ny][nx]
                    visit[ny][nx] = True

    print(f'#{t} {result}')