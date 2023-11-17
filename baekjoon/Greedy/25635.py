# 25635번 골드4 자유 이용권

'''
문제
https://www.acmicpc.net/problem/25635

입력
첫째 줄에 놀이기구의 종류의 개수 
$N(1\le N \le 100\ 000)$이 주어진다.

둘째 줄에 정수 
$a_1, a_2, ..., a_N$이 주어진다. 
$a_i(1 \le a_i \le 10^9)$는 
$i$번째 놀이기구 이용 횟수 제한이다.

출력
연속으로 같은 놀이기구를 이용하지 않고 놀이기구를 이용할 수 있는 최대 횟수를 출력한다.

예제 입력 1 
3
1 1 3
예제 출력 1 
5
예제 입력 2 
2
3 5
예제 출력 2 
7
예제 입력 3 
4
2 2 2 3
예제 출력 3 
9
'''

import sys
input = sys.stdin.readline

N = int(input())
park = sorted(list(map(int, input().split())))
# print(park)

if N == 1:
    print(1)
elif park[-1] <= sum(park[:N-1]) + 1:
    print(sum(park))
else:
    print(sum(park[:N-1])*2 + 1)