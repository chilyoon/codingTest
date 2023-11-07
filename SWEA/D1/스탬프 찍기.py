# 2046. 스탬프 찍기 D1

'''
주어진 숫자만큼 # 을 출력해보세요.

주어질 숫자는 100,000 이하다.

입력
3

출력
###

'''

import sys
sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

N = int(input())
print('#' * N)