# 1325번 실버1 효율적인 해킹

'''
효율적인 해킹 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
5 초	256 MB	69044	13255	8630	19.606%
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

예제 입력 1 
5 4
3 1
3 2
4 3
5 3
예제 출력 1 
1 2
'''

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

# 컴퓨터 번호 1~N, M개의 입력
N,M = map(int, input().split())
computer = [list(map(int, input().split())) for _ in range(M)]
maxResult = []
queue = deque()

def bfs(start):
    temp = 0
    queue.append(start)
    visit = [-1]*(N+1)
    visit[start] = 1
    while queue:
        x = queue.popleft()
        for i,j in computer:
            if x == j and visit[i] == -1:
                visit[i] == 1
                temp += 1
                queue.append(i)
    return temp
    
maxCnt = 1
for i in range(1,N+1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        maxResult.clear()
        maxResult.append(i)
    elif cnt == maxCnt:
        maxResult.append(i)

print(*maxResult)