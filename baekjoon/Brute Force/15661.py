# 15661번 골드5 링크와 스타트

'''
문제
https://www.acmicpc.net/problem/15661

입력
첫째 줄에 N(4 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

예제 입력 1 
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
예제 출력 1 
0
예제 입력 2 
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
예제 출력 2 
2
예제 입력 3 
8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
예제 출력 3 
1
예제 입력 4 
5
0 3 1 1 1
3 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
예제 출력 4 
0

PyPy3으로 시간초과 해결
'''

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations as com

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

ans = 10000000
for i in range(1, n//2 + 1):
    # print(f'i {i}')
    for team in com(range(n), i):
        # print(f'team {team}')
        start, link = 0,0
        linkT = []
        for j in range(n):
            if j in team:
                for k in team:
                    start += ability[j][k]
            else:
                linkT.append(j)
        for j in linkT:
            for k in linkT:
                link += ability[j][k]
        gap = abs(start - link)
        # print(f'start {start} link {link} gap {gap}')
        if gap < ans:
            ans = gap

print(ans)