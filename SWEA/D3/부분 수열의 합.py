# 2817. 부분 수열의 합 D3

'''
[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 2개의 자연수 N(1 ≤ N ≤ 20)과 K(1 ≤ K ≤ 1000)가 주어진다.

두 번째 줄에는 N개의 자연수 수열 A가 주어진다. 수열의 원소인 N개의 자연수는 공백을 사이에 두고 주어지며, 1 이상 100 이하임이 보장된다.

[출력]

각 테스트 케이스마다 ‘#x ’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 부분 수열의 합이 K가 되는 경우의 수를 출력한다.

입력
1
4 3
1 2 1 2

출력
#1 4

'''

import sys
sys.stdin = open("../input.txt", "r")

T = int(input())

def dfs(hap,idx):
    global answer
    if hap == k:
        answer += 1
        return
    if hap > k:
        return
    for i in range(idx,n):
        if not visit[i]:
            visit[i] = True
            dfs(hap+a[i],i)
            visit[i] = False

for t in range(1,T+1):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    visit = [False] * n
    answer = 0
    dfs(0,0)

    print(f'#{t} {answer}')