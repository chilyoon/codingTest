# 1967번 골드4 트리의 지름

'''
문제
https://www.acmicpc.net/problem/1967
입력
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1 
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
예제 출력 1 
45
'''
'''
bfs를 두번 돌리면 된다.
첫번째는 루트에서 가장 먼 노드 탐색
두번째는 가장 먼 노드에서 가장 먼 노드 탐색
메모리 초과 주의
tree리스트와 visit리스트만으로 문제 해결이 가능하다.
리스트를 여러게 만들어 메모리 초과하는일이 없도록 할 것.

도움
https://recordofwonseok.tistory.com/299
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visit = [-1] * (n+1)
    visit[start] = 0
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for i,cost in tree[cur]:
            if visit[i] == -1:
                queue.append(i)
                visit[i] = visit[cur] + cost
    m = max(visit)
    return [visit.index(m),m]

# 노드의 개수 n
n = int(input())
tree = [[] for _ in range(n+1)]
# 부모 a 자식 b 가중치 c
for _ in range(n-1):
    a,b,c = map(int, input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

print(bfs(bfs(1)[0])[1])