# 1058번 실버2 친구

'''
문제
https://www.acmicpc.net/problem/1058

입력
첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

출력
첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.

예제 입력 1 
3
NYY
YNY
YYN
예제 출력 1 
2
예제 입력 2 
3
NNN
NNN
NNN
예제 출력 2 
0
예제 입력 3 
5
NYNNN
YNYNN
NYNYN
NNYNY
NNNYN
예제 출력 3 
4
예제 입력 4 
10
NNNNYNNNNN
NNNNYNYYNN
NNNYYYNNNN
NNYNNNNNNN
YYYNNNNNNY
NNYNNNNNYN
NYNNNNNYNN
NYNNNNYNNN
NNNNNYNNNN
NNNNYNNNNN
예제 출력 4 
8
예제 입력 5 
15
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNYNNNNNNN
NNNNNNNYNNNNNNY
NNNNNNNNNNNNNNY
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNYYNNNNNNNNNNN
NNNNNYNNNNNYNNN
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
YNNYYNNNNYNNNNN
예제 출력 5 
6
예제 입력 6
6
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN
예제 출력 6
5
'''

import sys
input = sys.stdin.readline

'''
# BFS 방식
# from collections import deque

# N = int(input())
# friend = [list(input()) for _ in range(N)]
# ans = 0

# for i in range(N):
#     queue = deque([(i,0)])
#     visit = [False] * N
#     visit[i] = True
#     cnt = 0
#     while queue:
#         cur,deep = queue.popleft()
#         for j in range(N):
#             if not visit[j] and friend[cur][j] == 'Y' and deep < 2:
#                 # print(f'{cur}과 {j}는 친구')
#                 queue.append((j,deep+1))
#                 visit[j] = True
#                 cnt += 1
#     if cnt > ans:
#         ans = cnt
#     # print('==========')

# print(ans)
'''

# 백트래킹 방식
N = int(input())
friend = [list(input()) for _ in range(N)]

def dfs(cur,deep):
    if deep >= 2:
        return
    for j in range(N):
        if friend[cur][j] == 'Y' and not visit[j]:
            # print(f'{cur}과 {j}는 친구')
            visit[j] = True
            sf[j] = True
            dfs(j,deep+1)
            visit[j] = False

ans,cnt = 0,0
visit = [False] * N
sf = [False] * N

for i in range(N):
    visit[i] = True
    sf = [False] * N
    dfs(i,0)
    # print('================')
    visit[i] = False
    for l in sf:
        if l:
            cnt += 1
    ans = cnt if cnt > ans else ans
    cnt = 0

print(ans)

'''
DFS 풀이 방식 -> 방문 처리가 되어야 해서
6
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN
을 해버리면 0 -> 1 -> 2에서 2가 방문처리 되어서
0 -> 2 -> 3 을 해야하는 상황에 2때문에 방문을 못함

# def dfs(idx,deep):
#     global ans,cnt
#     if cnt > ans:
#         ans = cnt
#     for j in range(N):
#         if friend[idx][j] == 'Y' and not visit[j] and deep < 2:
#             print(f'{idx}와 {j} 친구 cnt{cnt+1}')
#             visit[j] = True
#             cnt += 1
#             dfs(j,deep+1)
#             # visit[j] = False

# N = int(input())
# friend = [list(input().rstrip()) for _ in range(N)]

# visit = [False]*N

# ans,cnt = 0,0
# for i in range(N):
#     visit[i] = True
#     cnt = 0
#     dfs(i,0)
#     print('=======')
#     # visit[i] = False
#     visit = [False]*N

# print(ans)
'''