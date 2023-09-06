# 21937번 실버1 작업

'''
문제
https://www.acmicpc.net/problem/21937
입력
민상이가 작업할 개수 
$N$와 작업 순서 정보의 개수 
$M$이 공백으로 구분되어 주어진다.

두 번째줄부터 
$M + 1$ 줄까지 작업 
$A_i$와 작업 
$B_i$가 공백으로 구분되어 주어진다. 이때 두 값의 의미는 작업 
$B_i$를 하기 위해서 바로 이전에 작업 
$A_i$를 먼저 해야한다는 의미이다. 중복된 정보는 주어지지 않는다.

마지막 줄에는 민상이가 오늘 반드시 끝내야하는 작업 
$X$가 주어진다.

출력
민상이가 작업 
$X$를 하기 위해 먼저 해야하는 일의 개수를 출력한다.

제한
 
$1 \le N \le 100,000$ 
 
 
$0 \le M \le min( \frac {N×(N - 1)} {2}, 200000)$ 
 
$1 \le A_i, B_i \le N$ 
 
$1 \le X \le N$ 
예제 입력 1 
6 4
1 6
2 4
4 6
4 5
5
예제 출력 1 
2
예제 입력 2 
6 4
1 6
2 4
4 6
4 5
3
예제 출력 2 
0
예제 입력 3 
4 4
1 2
1 3
2 4
3 4
4
예제 출력 3 
3
'''

import sys
from collections import deque
input = sys.stdin.readline

# 작업할 개수 N 작업 순서 정보의 개수 M
N,M = map(int, input().split())
work = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    work[b].append(a)

visit = [-1] * (N+1)
X = int(input())
visit[X] = 0
queue = deque([X])

cnt = 0
while queue:
    num = queue.popleft()
    for i in work[num]:
        if visit[i] == -1:
            visit[i] = visit[num] + 1
            cnt += 1
            queue.append(i)

print(cnt)