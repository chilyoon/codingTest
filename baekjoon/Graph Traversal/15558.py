# 15558번 골드5 점프 게임

'''
문제
https://www.acmicpc.net/problem/15558

입력
첫째 줄에 N과 k가 주어진다. (1 ≤ N, k ≤ 100,000)

둘째 줄에는 왼쪽 줄의 정보가 주어진다. i번째 문자가 0인 경우에는 위험한 칸이고, 1인 경우에는 안전한 칸이다. 셋째 줄에는 오른쪽 줄의 정보가 주어지고, 각 문자의 의미는 왼쪽 줄의 의미와 동일하다.

왼쪽 줄의 1번 칸은 항상 안전한 칸이다.

출력
게임을 클리어할 수 있으면 1을, 없으면 0을 출력한다.

예제 입력 1 
7 3
1110110
1011001
예제 출력 1 
1

예제 입력 2 
6 2
110101
011001
예제 출력 2 
0
'''

'''
queue에 시간을 같이 넣어야한다. 끝마다 시간을 +=1 해버리니 같은 시간에도 더해져버려 문제 발생
'''

import sys
from collections import deque
input = sys.stdin.readline

# n칸, k칸 앞의 칸으로 이동
n,k = map(int, input().split())
jump = [list(map(int, input().rstrip()))+[1]*k for _ in range(2)]
visit = [[False]*(n+k) for _ in range(2)]
visit[0][0] = True

dx,dy = [1,-1,k],[0,0,1]

queue = deque([(0,0,0)])

def bfs():
    while queue:
        x,y,t = queue.popleft()
        # print('---------------------')
        # print(f'nx {x} ny {y} visit {visit[y][x]}')
        if x >= n-1:
            # result = 1
            # break
            return print(1)        
        for i in range(3):
            nx = x + dx[i]
            ny = (y + dy[i])%2
            # print(nx,ny)
            if t < nx < n+k and jump[ny][nx] == 1 and not visit[ny][nx]:
                # print(f'nx {nx} ny {ny} visit {visit[ny][nx]}')
                visit[ny][nx] = True
                queue.append((nx,ny,t+1))
    print(0)

bfs()