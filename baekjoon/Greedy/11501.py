# 11501번 실버2 주식

'''
문제
https://www.acmicpc.net/problem/11501

입력
입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

출력
각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.

예제 입력 1 
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
예제 출력 1 
0
10
5
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
      n = int(input())
      ju = list(map(int, input().split()))

      money = 0
      cur = ju[-1]
      for i in range(n-2,-1,-1):
            if cur > ju[i]:
                  money += (cur-ju[i])
            elif cur < ju[i]:
                  cur = ju[i]
      
      print(money)