# 21318번 실버1 피아노 체조

'''
문제
https://www.acmicpc.net/problem/21318
입력
첫 번째 줄에 악보의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.

두 번째 줄에 1번 악보부터 N번 악보까지의 난이도가 공백을 구분으로 주어진다.

세 번째 줄에 질문의 개수 Q(1 ≤ Q ≤ 100,000)이 주어진다.

다음 Q개의 줄에 각 줄마다 두 개의 정수 x, y(1 ≤ x ≤ y ≤ N)가 주어진다.

출력
x번부터 y번까지의 악보를 순서대로 연주할 때, 몇 개의 악보에서 실수하게 될지 0 이상의 정수 하나로 출력한다. 각 출력은 개행으로 구분한다.

예제 입력 1 
9
1 2 3 3 4 1 10 8 1
5
1 3
2 5
4 7
9 9
5 9
예제 출력 1 
0
0
1
0
3
예제 입력 2 
6
573 33283 5572 346 906 567
5
5 6
1 3
2 2
1 6
3 6
예제 출력 2 
1
1
0
3
2
'''

import sys
input = sys.stdin.readline

# 악보의 개수 
N = int(input())
# 악보 sheet
sheet = list(map(int, input().split()))
miss = 0
psum = [0]
for i in range(N):
    if i == N-1:
        psum.append(miss)
        break
    if sheet[i] > sheet[i+1]:
        miss += 1
    psum.append(miss)
# print(psum)

# 질문의 개수 Q
Q = int(input())   
for _ in range(Q):
    x,y = map(int ,input().split())
    ssum = psum[y-1]-psum[x-1]
    print(ssum)