# 20438번 실버2 출석체크

'''
문제
https://www.acmicpc.net/problem/20438
입력
1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)

2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과 Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.

4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)

출력
M개의 줄에 걸쳐서 각 구간에 대해서 출석이 되지 않은 학생들의 수를 출력하라.

예제 입력 1 
10 1 3 1
7
3 5 7
3 12
예제 출력 1 
4
입장 번호 3번부터 12번까지의 구간에서 입장 번호 4, 8, 11번이 출석 코드를 받지 못했고, 7번은 출석 코드를 받았으나 조느라 출석하지 못했다.

예제 입력 2 
50 4 5 1
24 15 27 43
3 4 6 20 25
3 52
예제 출력 2 
25

예제 입력 3
5 1 1 1
3
3
3 7
예제 출력 3
5
'''

import sys
input = sys.stdin.readline

# 학생 N 졸고있는 학생 K 출석 코드 보낼 학생 Q 주어질 구간 M
N,K,Q,M = map(int, input().split())
sleep = list(map(int, input().split()))
card = list(map(int, input().split()))

student = [1]*(N+3)
psum = [0]*(N+3)

for i in card:
    # 첫 카드를 주는 학생이 졸면 전달해주지 않는다.
    # 3 -> 6 -> 9 가 아니라 3 -> 6,9 방식
    if i in sleep:
        continue
    for j in range(i,N+3,i):
        if j in sleep:
            continue
        else:
            student[j] = 0

for i in range(3,N+3):
    psum[i] = psum[i-1] + student[i]

# print(psum)
# print(student)

for _ in range(M):
    S,E = map(int ,input().split())
    # 3 ~ 12번이라면 12번 인덱스부터 3번 인덱스 까지라서 2번 인덱스로 빼야한다.
    print(psum[E]-psum[S-1])
