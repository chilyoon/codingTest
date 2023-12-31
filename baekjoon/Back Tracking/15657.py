# 15657번 실버3 N과 M (8)

'''
문제
https://www.acmicpc.net/problem/15657
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 5 2
예제 출력 1 
2
4
5
예제 입력 2 
4 2
9 8 7 1
예제 출력 2 
1 1
1 7
1 8
1 9
7 7
7 8
7 9
8 8
8 9
9 9
예제 입력 3 
4 4
1231 1232 1233 1234
예제 출력 3 
1231 1231 1231 1231
1231 1231 1231 1232
1231 1231 1231 1233
1231 1231 1231 1234
1231 1231 1232 1232
1231 1231 1232 1233
1231 1231 1232 1234
1231 1231 1233 1233
1231 1231 1233 1234
1231 1231 1234 1234
1231 1232 1232 1232
1231 1232 1232 1233
1231 1232 1232 1234
1231 1232 1233 1233
1231 1232 1233 1234
1231 1232 1234 1234
1231 1233 1233 1233
1231 1233 1233 1234
1231 1233 1234 1234
1231 1234 1234 1234
1232 1232 1232 1232
1232 1232 1232 1233
1232 1232 1232 1234
1232 1232 1233 1233
1232 1232 1233 1234
1232 1232 1234 1234
1232 1233 1233 1233
1232 1233 1233 1234
1232 1233 1234 1234
1232 1234 1234 1234
1233 1233 1233 1233
1233 1233 1233 1234
1233 1233 1234 1234
1233 1234 1234 1234
1234 1234 1234 1234
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


## -> 현재 back리스트가 sorted했을때랑 같은가? 아니라면 비내림차순이 아니다.
## 하지만 다 넣고 비교해서 시간이 좀 더 걸림
# def dfs():
#     if len(back) == M:
#         print(*back)
#         return
#     else:
#         for i in sequence:
#             back.append(i)
#             if back == sorted(back):
#                 dfs()
#             back.pop()

# N,M = map(int, input().split())
# sequence = sorted(list(map(int, input().split())))
# back = []

# dfs()

## -> 인덱스도 넣어서 비교 인덱스를 바로 넣어 불필요한 값을 넣을 필요가 없다.
def dfs(len, idx):
    if len == M:
        print(*back)
        return
    for i in range(idx,N):
        back.append(sequence[i])
        dfs(len+1, i)
        back.pop()

N,M = map(int ,input().split())
sequence = sorted(list(map(int, input().split())))
back = []

for i in range(N):
    back.append(sequence[i])
    dfs(1, i)
    back.pop()