# 2304번 실버2 창고 다각형

'''
문제
https://www.acmicpc.net/problem/2304

입력
첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. N은 1 이상 1,000 이하이다. 그 다음 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H가 한 개의 빈 칸을 사이에 두고 주어진다. L과 H는 둘 다 1 이상 1,000 이하이다.

출력
첫 줄에 창고 다각형의 면적을 나타내는 정수를 출력한다.

예제 입력 1 
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
예제 출력 1 
98
예제 입력 2
5
4 3
6 5
9 5
11 3
13 4
예제 출력 2
42

-> 가장 높은 크기를 찾고 양옆으로 넓이를 구해야함 가장 높은 크기는 하나만 있지 않다.
'''

import sys
input = sys.stdin.readline

n = int(input())
col = [list(map(int, input().split())) for _ in range(n)]
col.sort()

mH = 0
mL = []
for i in range(n):
    if col[i][1] > mH:
        mH = col[i][1]
        mL = [i]
    elif col[i][1] == mH:
        mL += [i]

ans = 0
l,h = col[0][0],col[0][1]
for i in range(mL[0]+1):
    if col[i][1] > h:
        ans += (col[i][0] - l) * h 
        l = col[i][0]
        h = col[i][1]

ans += (col[mL[-1]][0] - col[mL[0]][0] + 1) * mH

L,H = col[-1][0], col[-1][1]
for i in range(n-1, mL[-1]-1, -1):
    if col[i][1] > H:
        ans += (L - col[i][0]) * H
        L = col[i][0]
        H = col[i][1]

print(ans)