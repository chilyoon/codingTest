# 21919번 실버3 소수 최수 공배수

'''
문제
https://www.acmicpc.net/problem/21919

입력
첫째 줄에 수열 
$A$의 길이 
$N$이 주어진다. 
$(1 \le N \le 10,000)$ 

그 다음줄에는 수열 
$A$의 원소 
$A_{i}$가 공백으로 구분되어 주어진다. 
$(2 \le A_{i} \le 1,000,000)$ 

답이 263 미만인 입력만 주어진다.

출력
첫째 줄에 소수들의 최소공배수를 출력한다.

만약 소수가 없는 경우는 -1을 출력한다.

예제 입력 1 
5
2 3 5 6 8
예제 출력 1 
30
수열 중에 소수는 2, 3, 5가 있다.

예제 입력 2 
4
4 16 64 256
예제 출력 2 
-1
소수가 없으므로 -1 이다.
'''

import sys
input = sys.stdin.readline

n = int(input())
A = list(set(map(int, input().split())))
ans = 1

for i in A:
    flag = True
    if i != 2 and i % 2 == 0:
        flag = False
    else:
        for j in range(3,i,2):
            if i % j == 0:
                flag = False
                break
    if flag:
        ans *= i

print(-1 if ans == 1 else ans)