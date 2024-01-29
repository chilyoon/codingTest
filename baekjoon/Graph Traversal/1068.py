# 1068번 골드5 트리

'''
문제
https://www.acmicpc.net/problem/1068

--> 루트가 단말이 될 수 있다. 루트가 삭제되면 답은 무조건 0

입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

예제 입력 1 
5
-1 0 0 1 1
2
예제 출력 1 
2
예제 입력 2 
5
-1 0 0 1 1
1
예제 출력 2 
1
예제 입력 3 
5
-1 0 0 1 1
0
예제 출력 3 
0
예제 입력 4 
9
-1 0 0 2 2 4 4 6 6
4
예제 출력 4 
2
예제 입력 5
5
1 2 3 4 -1
3
예제 출력 5
1
'''


import sys
input = sys.stdin.readline
from collections import deque

# 0 ~ n-1
n = int(input())
visit = [False] * n
tree = list(map(int, input().split()))
graph = [[] for _ in range(n)]

start = -1
queue = deque()
for i in range(n):
    if tree[i] == -1:
        queue.append(i)
        start = i
        visit[i] = True
        continue
    graph[i].append(tree[i])
    graph[tree[i]].append(i)

rem = int(input())
if start == rem:
    print(0)
    sys.exit()

graph[rem].clear()
# print(*graph)

cnt = 0
while queue:
    cur = queue.popleft()
    # print(f'cur {cur}')
    flag = True
    for i in graph[cur]:
        if not visit[i] and cur in graph[i]:
            # print(f'i {i}')
            # cnt += 1
            visit[i] = True
            queue.append(i)
            flag = False
    if flag:
        cnt += 1
print(cnt) 

