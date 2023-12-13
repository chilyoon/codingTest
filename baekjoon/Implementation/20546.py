# 20546번 실버5 🐜 기적의 매매법 🐜

'''
문제
https://www.acmicpc.net/problem/20546

입력
첫 번째 줄에 준현이와 성민이에게 주어진 현금이 주어진다.

두 번째 줄에 2021년 1월 1일부터 2021년 1월 14일까지의 MachineDuck 주가가 공백을 두고 차례대로 주어진다. 모든 입력은 1000 이하의 양의 정수이다.

출력
1월 14일 기준 준현이의 자산이 더 크다면 "BNP"를, 성민이의 자산이 더 크다면 "TIMING"을 출력한다.

둘의 자산이 같다면 "SAMESAME"을 출력한다. 모든 결과 따옴표를 제외하고 출력한다.

예제 입력 1 
100
10 20 23 34 55 30 22 19 12 45 23 44 34 38
예제 출력 1 
BNP
준현이는 1월 1일에 10주를 매수한다. 따라서 1월 14일 380원의 자산을 가지게 된다.

성민이는 1월 8일에 5주를 매수한다. 따라서 1월 14일 195원의 자산을 가지게 된다.

예제 입력 2 
15
20 20 33 98 15 6 4 1 1 1 2 3 6 14
예제 출력 2 
TIMING
준현이는 1월 5일에 1주를 매수한다. 따라서 14일의 자산은 14원이다.

성민이는 1월 7일 3주를, 1월 8일 3주를 매수한다. 그리고 1월 13일에 전량 매도한다. 따라서 14일 자산은 36원이다.
'''

import sys
input = sys.stdin.readline

money = int(input())
duck = list(map(int, input().split()))

jh, sm = 0, 0
jhM, smM = money, money

for i in range(13):
    ju = jhM // duck[i]
    if ju > 0:
        jh += ju
        jhM -= (duck[i]*ju)

jhM += (duck[-1] * jh)

for i in range(11):
    # 3일 연속 하락 전량 매수
    if duck[i] > duck[i+1] > duck[i+2] > duck[i+3]:
        sm += (smM // duck[i+3])
        smM -= ((smM // duck[i+3]) * duck[i+3])
    # 3일 연속 상승 전량 매도
    if sm > 0 and duck[i] < duck[i+1] < duck[i+2] < duck[i+3]:
        smM += (sm*duck[i+3])
        sm = 0

smM += (duck[-1] * sm)

# print(jhM, smM)
if jhM > smM:
    print('BNP')
elif jhM < smM:
    print('TIMING')
else:
    print('SAMESAME')