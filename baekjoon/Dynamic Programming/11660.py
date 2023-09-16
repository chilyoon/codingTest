# 11660번 실버1 구간 합 구하기

'''
문제
https://www.acmicpc.net/problem/11660
입력
첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)

출력
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

예제 입력 1 
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
예제 출력 1 
27
6
64
예제 입력 2 
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
예제 출력 2 
1
2
3
4
예제 입력 3
5 1
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
4 3 5 5
예제 출력 3
129
'''

import sys
input = sys.stdin.readline

# 크키 N 구해야 하는 횟수 M
N,M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
psum = [[0]*(N+1) for _ in range(N+1)]
# 누적 합 구하기
for i in range(1,N+1):
    for j in range(1,N+1):
        psum[i][j] = table[i-1][j-1] + psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1]

# print(*psum, sep='\n')
for _ in range(M):
    y1,x1,y2,x2 = map(int ,input().split())
    # 구간 합 구하기
    print(psum[y2][x2] - psum[y2][x1-1] - psum[y1-1][x2] + psum[y1-1][x1-1])