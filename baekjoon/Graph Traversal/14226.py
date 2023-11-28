# 14226번 골드4 이모티콘

'''
문제
https://www.acmicpc.net/problem/14226

입력
첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.

출력
첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.

예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
4
예제 출력 2 
4
예제 입력 3 
6
예제 출력 3 
5
예제 입력 4 
18
예제 출력 4 
8
반례 모음
# N [정답,오답]
217 [18, 19] x
325 [19, 21] o
497 [20, 21] x
505 [20, 21] o
553 [21, 22] x
651 [21, 22] x
687 [21, 22] o
973 [23, 24] x
975 [22, 23] o
994 [22, 23] x

-> cnt와 clip을 같이 visit처리해서 구해야함
'''

import sys
input = sys.stdin.readline
from collections import deque

s = int(input())
# 화면 이모티콘 개수, 시간, 클립보드
queue = deque([(1,0,0)])
visit = set()
cv = set()

while queue:
    # print(queue)
    cnt,t,clip = queue.popleft()
    if cnt == s:
        print(t)
        break
    if cnt not in cv:
        queue.append((cnt,t+1,cnt))
        cv.add(cnt)
    for i in [cnt+clip, cnt-1]:
        if 1 < i <= 2000 and (i,clip) not in visit:
            queue.append((i,t+1,clip))
            visit.add((cnt,clip))