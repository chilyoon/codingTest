# 9663번 골드4 N-Queen

'''
문제
https://www.acmicpc.net/problem/9663
입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
'''

import sys
input = sys.stdin.readline

def check(y):
    for i in range(y):
        # visit로 가로세로를 확인했기 때문에 대각선만 확인하면 된다.
        if abs(chess[y] - chess[i]) == y - i:
            return False
    return True

def dfs(y):
    global cnt
    if y == N:
        cnt += 1
        return
    for i in range(N):
        if not visit[i]:
            chess[y] = i
            if check(y):
                visit[i] = True
                dfs(y+1)
                visit[i] = False

N = int(input())
chess = [0] * N
visit = [False] * N
cnt = 0

dfs(0)
print(cnt)