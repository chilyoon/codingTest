# 18513번 골드4 샘터

'''
문제
https://www.acmicpc.net/problem/18513
입력
첫째 줄에 자연수 N과 K가 공백을 기준으로 구분되어 주어진다. (1 ≤ N, K ≤ 100,000) 둘째 줄에 N개의 샘터의 위치가 공백을 기준으로 구분되어 정수 형태로 주어진다. (-100,000,000 ≤ 샘터의 위치 ≤ 100,000,000) 단, 모든 N개의 샘터의 위치들은 서로 다르게 주어진다.

출력
첫째 줄에 모든 집에 대한 불행도의 합의 최솟값을 출력한다.

예제 입력 1 
2 5
0 3
예제 출력 1 
6
'''

import sys
from collections import deque
input = sys.stdin.readline

# N개의 샘터 K채의 집
N,K = map(int, input().split())
visit = dict()
queue = deque()
sum = 0
water = list(map(int, input().split()))
# 샘물 위치를 입력받은 후 방문 처리
for i in water:
    visit[i] = 0
    queue.append(i)
    
home = 0
while queue:
    x = queue.popleft()
    for i in [-1,1]:
        nx = x + i
        # 범위 문제 똑바로 읽기
        if nx not in visit:
            visit[nx] = visit[x] + 1
            sum += visit[nx]
            queue.append(nx)
            home += 1
            if home == K:
                print(sum)
                sys.exit()
