# 5215. 햄버거 다이어트 D3

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 재료의 수, 제한 칼로리를 나타내는 N, L(1 ≤ N ≤ 20, 1 ≤ L ≤ 104)가 공백으로 구분되어 주어진다.

다음 N개의 줄에는 재료에 대한 민기의 맛에 대한 점수와 칼로리를 나타내는 Ti, Ki(1 ≤ Ti ≤ 103, 1 ≤ Ki ≤ 103)가 공백으로 구분되어 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수를 출력한다.

입력
1
5 1000
100 200
300 500
250 300
500 1000
400 400

출력
#1 750

'''

import sys
sys.stdin = open("../input.txt", "r")

Test = int(input())

def dfs(cnt, cal, sco):
    global score
    if cal > L:
        return
    if sco > score:
        score = sco
    if cnt == N:
        return

    dfs(cnt+1,cal+calorie[cnt],sco+taste[cnt])
    dfs(cnt+1,cal,sco)


for t in range(1,Test+1):
    # 재료 수 N 제한 칼로리 L
    N,L = map(int, input().split())
    # 맛 점수 T, 칼로리 K
    taste, calorie = [],[]
    for _ in range(N):
        T,K = map(int, input().split())
        taste += [T]
        calorie += [K]

    score = 0

    dfs(0,0,0)
    print(f'#{t} {score}')