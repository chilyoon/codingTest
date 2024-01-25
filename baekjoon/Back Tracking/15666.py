# 15666번 실버2 N과 M (12)

'''
문제
https://www.acmicpc.net/problem/15666

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력 1 
3 1
4 4 2
예제 출력 1 
2
4
예제 입력 2 
4 2
9 7 9 1
예제 출력 2 
1 1
1 7
1 9
7 7
7 9
9 9
예제 입력 3 
4 4
1 1 2 2
예제 출력 3 
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2
'''

import sys
input = sys.stdin.readline

def dfs(cnt,idx):
    if cnt == m:
        print(*seq)
        return
    for i in range(idx,len(N)):
        seq.append(N[i])
        dfs(cnt+1,i)
        seq.pop()

# n개중 m개 고름
n,m = map(int, input().split())
N = sorted(set(map(int, input().split())))

seq = []
dfs(0,0)