# 2665번 골드4 미로만들기

'''
문제
https://www.acmicpc.net/problem/2665

입력
첫 줄에는 한 줄에 들어가는 방의 수 n(1 ≤ n ≤ 50)이 주어지고, 다음 n개의 줄의 각 줄마다 0과 1이 이루어진 길이가 n인 수열이 주어진다. 0은 검은 방, 1은 흰 방을 나타낸다.

출력
첫 줄에 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.

예제 입력 1 
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
예제 출력 1 
2
예제 입력 2
7
1001111
0001001
1001000
1001001
1001000
1001000
1111001
예제 출력 2
3
예제 입력 3
5
10111
10101
10101
10101
11101
예제 출력 3
0

완전 탐색 하면서 같은 곳을 방문해도 벽을 뚫은 수가 적은걸 반영하도록 풀어야함
'''
import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 방문 안했을때
                if visit[ny][nx] == -1:
                    if room[ny][nx] == 1:
                        visit[ny][nx] = visit[y][x]
                    else:
                        visit[ny][nx] = visit[y][x] + 1
                    queue.append((nx,ny))
                # 방문 했을때
                else:
                    if room[ny][nx] == 1 and visit[ny][nx] > visit[y][x]:
                        visit[ny][nx] = visit[y][x]
                        queue.append((nx,ny))
                    elif room[ny][nx] == 0 and visit[ny][nx] > visit[y][x] + 1:
                        visit[ny][nx] = visit[y][x] + 1
                        queue.append((nx,ny))

# n x n
n = int(input())
# 0 검은방 1 흰 방
room = [list(map(int, input().rstrip())) for _ in range(n)]
# print(room)
visit = [[-1]*n for _ in range(n)]
visit[0][0] = 0
queue = deque([(0,0)])

bfs()
print(visit[n-1][n-1])