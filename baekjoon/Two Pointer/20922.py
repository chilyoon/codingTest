# 20922번 실버1 겹치는 건 싫어

'''
문제
https://www.acmicpc.net/problem/20922

입력
첫째 줄에 정수 N(1 <= N <= 200000)과 K(1 <= K <= 100)가 주어진다.

둘째 줄에는 a1,a2,a3...an이 주어진다(1<=ai<=100000)

출력
조건을 만족하는 최장 연속 부분 수열의 길이를 출력한다.

예제 입력 1 
9 2
3 2 5 5 6 4 4 5 7
예제 출력 1 
7
예제 입력 2 
10 1
1 2 3 4 5 6 6 7 8 9
예제 출력 2 
6
노트
연속 부분 수열이란 그 수열의 원소를 하나 이상 연속하여 선택한 부분 수열을 말한다.
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

n,k = map(int, input().split())
sequence = list(map(int, input().split()))
subseq = defaultdict(int)

L,R = 0,0
mL,cnt = 0,0
while R < n:
    if subseq[sequence[R]] + 1 <= k:
        subseq[sequence[R]] += 1
        R += 1
        cnt += 1
        mL = max(mL, cnt)
    else:
        subseq[sequence[L]] -= 1
        if subseq[sequence[L]] == 0:
            del subseq[sequence[L]]
        L += 1
        cnt -= 1
    
print(mL)