# 13549번 골드5 숨바꼭질3

'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
2
힌트
수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.
'''

import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())
visit = [False] * 100001
queue = deque([(N,0)])

while queue:
    cur, time = queue.popleft()
    if cur == K:
        print(time)
        sys.exit()
    visit[cur] = True
    # 반복의 순서 --> 낮은 시간부터 적용
    for i,t in ((cur*2,0), (cur-1,1), (cur+1,1)):
        if 0 <= i <= 100000:
            if not visit[i]:
                queue.append((i,time+t))