# 12851번 골드4 숨바꼭질2

'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
2
'''

import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())
visit = [False] * 100001
visit[N] = True
queue = deque([(N,0)])

cnt = 1

while queue:
    cur, time = queue.popleft()
    visit[cur] = True
    if cur == K:
        print(time)
        if time == 0:
            print(1)
            sys.exit()
        for i,j in queue:
            if i == cur and j == time:
                cnt += 1
        print(cnt)
        sys.exit()
    for i in (cur-1, cur+1, cur*2):
        if 0 <= i <= 100000:
            if not visit[i]:
                queue.append((i, time+1))