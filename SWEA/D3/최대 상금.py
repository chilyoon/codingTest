# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

[입력]

가장 첫 줄은 전체 테스트 케이스의 수이다.

최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.

각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.

숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

[출력]

각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.

같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.

입력
3
123 1
2737 1
32888 2

출력
#1 321
#2 7732
#3 88832

'''

import sys
sys.stdin = open("../input.txt", "r")
#
# from collections import defaultdict
#
# T = int(input())
#
# def dfs(count):
#     global answer
#     if count == 0:
#         answer = max(int("".join(num)),answer)
#         return
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             num[i],num[j] = num[j],num[i]
#             temp = "".join(num)
#             # 딕셔너리에 있다면 0 반환 아니면 1 반환
#             if visit.get((temp,count-1),1):
#                 visit[(temp,count-1)] = 0
#                 dfs(count-1)
#             num[i], num[j] = num[j], num[i]
#
#
# for t in range(1,T+1):
#     num, change = map(int, input().split())
#     num = list(str(num))
#     answer = -1
#     visit = defaultdict()
#     dfs(change)
#     print(f'#{t} {answer}')


def dfs(cnt):
    global answer
    if cnt == 0:
        answer = max(int("".join(num)), answer)
        return

    for i in range(len(num)):
        for j in range(i+1,len(num)):
            num[i],num[j] = num[j],num[i]
            number = int("".join(num))
            if (number,cnt) not in visit:
                visit.append((number,cnt))
                dfs(cnt-1)
                # visit.remove(number)
            num[i],num[j] = num[j],num[i]

T = int(input())

for t in range(1,T+1):
    num, change = map(int, input().split())
    num = list(str(num))
    answer = 0
    visit = []
    dfs(change)
    print(f'#{t} {answer}')