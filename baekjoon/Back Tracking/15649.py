# 15649번 실버3 N과 M (1)

'''
문제
https://www.acmicpc.net/problem/15649
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
예제 출력 1 
1
2
3
예제 입력 2 
4 2
예제 출력 2 
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
예제 입력 3 
4 4
예제 출력 3 
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1
'''

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs():
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(1,N+1):
        if i not in sequence and len(sequence) < M:
            sequence.append(i)
            dfs()
            sequence.pop()

N,M = map(int, input().split())
sequence = []
for i in range(1,N+1):
    sequence.append(i)
    dfs()
    sequence.pop()