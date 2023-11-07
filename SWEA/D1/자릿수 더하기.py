# 2058. 자릿수 더하기 D1

'''
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.


[제약 사항]

자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)


[입력]

입력으로 자연수 N이 주어진다.


[출력]

각 자릿수의 합을 출력한다.

입력
6789

출력
30
'''

import sys
sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

N = str(input())
sum = 0
for i in range(len(N)):
    sum += int(N[i])

print(sum)