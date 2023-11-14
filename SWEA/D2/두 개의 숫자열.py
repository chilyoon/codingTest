# 1959. 두 개의 숫자열 D2

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

[제약 사항]

N 과 M은 3 이상 20 이하이다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

두 번째 줄에는 Ai,

세 번째 줄에는 Bj 가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
10
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3

출력
#1 30
#2 63

'''

import sys
sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1,T+1):
    # N,M개의 숫자열
    N,M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    long_list = []
    short_list = []
    if N > M:
        long_list = Ai
        short_list = Bj
    elif M > N:
        long_list = Bj
        short_list = Ai
    else:
        esum = 0
        for i in range(len(Ai)):
            esum += (Ai[i] * Bj[i])
        print('#%d %d' % (t, esum))
        continue

    max_num = 0
    for i in range(len(long_list)-len(short_list)+1):
        sum = 0
        for j in range(0, len(short_list)):
            sum += long_list[i+j] * short_list[j]
        if sum > max_num:
            max_num = sum

    print('#%d %d' % (t,max_num))