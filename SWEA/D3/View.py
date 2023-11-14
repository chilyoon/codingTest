# 1206. [S/W 문제해결 기본] 1일차 - View D3

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

[제약 사항]

가로 길이는 항상 1000이하로 주어진다.

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)

각 빌딩의 높이는 최대 255이다.

[입력]

총 10개의 테스트케이스가 주어진다.

각 테스트케이스의 첫 번째 줄에는 건물의 개수 N이 주어진다. (4 ≤ N ≤ 1000)

그 다음 줄에는 N개의 건물의 높이가 주어진다. (0 ≤ 각 건물의 높이 ≤ 255)

맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)

[출력]

#부호와 함께 테스트케이스의 번호를 출력하고, 공백 문자 후 조망권이 확보된 세대의 수를 출력한다.
입력
100
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 ...
1000
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 ...
...

출력
#1 691
#2 9092

'''

import sys
sys.stdin = open("../input.txt", "r")

for t in range(1,11):
    N = int(input())
    building = list(map(int, input().split()))
    cnt = 0
    for i in range(2,N-2):
        near = sorted(building[i-2:i+3], reverse=True)
        if near[0] == building[i]:
            cnt += (near[0]-near[1])

    print('#%d %d' % (t, cnt))