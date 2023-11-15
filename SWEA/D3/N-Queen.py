# 2806. N-Queen D3

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 자연수 N(1 ≤ N ≤ 10)이 주어진다.

[출력]

각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

입력
2
1
2

출력
#1 1
#2 0

'''

import sys
sys.stdin = open("../input.txt", "r")

def check(n):
    for i in range(n):
        if abs(chess[n]-chess[i]) == n-i:
            return False
    return True

def dfs(n):
    global answer
    if n == N:
        answer += 1
        return
    for i in range(N):
        if not visit[i]:
            chess[n] = i
            if check(n):
                visit[i] = True
                dfs(n+1)
                visit[i] = False

T = int(input())

for t in range(1,T+1):
    N = int(input())
    chess = [0] * N
    visit = [False] * N
    answer = 0
    dfs(0)
    print(f'#{t} {answer}')