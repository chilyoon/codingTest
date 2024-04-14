# 2164번 실버4 카드2

'''
문제
https://www.acmicpc.net/problem/2164

입력
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

출력
첫째 줄에 남게 되는 카드의 번호를 출력한다.

예제 입력 1 
6
예제 출력 1 
4

--> 큐로 푸는 문제
'''

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
num = deque()
for i in range(1,n+1):
    num += [i]

step = True
while len(num) > 1:
    if step:
        num.popleft()
    else:
        num += [num.popleft()]
    step = not step

print(*num)