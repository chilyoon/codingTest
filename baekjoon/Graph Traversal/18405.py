# 18405번 골드5 경쟁적 전염

'''
문제
https://www.acmicpc.net/problem/18405

입력
첫째 줄에 자연수 N, K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N ≤ 200, 1 ≤ K ≤ 1,000) 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다. 각 행은 N개의 원소로 구성되며, 해당 위치에 존재하는 바이러스의 번호가 공백을 기준으로 구분되어 주어진다. 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또한 모든 바이러스의 번호는 K이하의 자연수로만 주어진다. N+2번째 줄에는 S, X, Y가 공백을 기준으로 구분되어 주어진다. (0 ≤ S ≤ 10,000, 1 ≤ X, Y ≤ N)

출력
S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력한다. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.

예제 입력 1 
3 3
1 0 2
0 0 0
3 0 0
2 3 2
예제 출력 1 
3
예제 입력 2 
3 3
1 0 2
0 0 0
3 0 0
1 2 2
예제 출력 2 
0

--> 판이 다채워졌는데 시간이 안끝날 경우 확인
'''

import sys
input = sys.stdin.readline
from collections import deque

dx,dy = [0,0,-1,1],[-1,1,0,0]

# n개의 원소, k이하의 바이러스 번호
n,k = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(n)]
# s초 x,y바이러스
s,Y,X = map(int, input().split())
queue = deque()

for num in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if virus[i][j] == num:
                # 바이러스 번호, (x,y)
                queue.append((num,j,i,0))


while queue:
    num,x,y,t = queue.popleft()
    # print(queue)
    # print(*virus,sep='\n')
    # print()

    if t== s:
        print(virus[Y-1][X-1])
        sys.exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and virus[ny][nx] == 0:
            virus[ny][nx] = num
            queue.append((num,nx,ny,t+1))

print(virus[Y-1][X-1])