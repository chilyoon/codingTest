# 20207번 골드5 달력

'''
문제
https://www.acmicpc.net/problem/20207

입력
첫째 줄에 일정의 개수 N이 주어진다. (1 ≤ N ≤ 1000)

둘째 줄부터 일정의 개수만큼 시작 날짜 S와 종료 날짜 E가 주어진다. (1 ≤ S ≤ E ≤ 365)

출력
코팅지의 면적을 출력한다.

예제 입력 1 
7
2 4
4 5
5 6
5 7
7 9
11 12
12 12
예제 출력 1 
28
예제 입력 2 
5
1 9
8 9
4 6
3 4
2 5
예제 출력 2 
36
예제 입력 3
1
1 365
예제 출력 3
365
'''

import sys
input = sys.stdin.readline

n = int(input())
day = [0] * 366
for _ in range(n):
    s,e = map(int, input().split())
    for i in range(s,e+1):
        day[i] += 1

cnt, ans, deep = 0, 0, 0
for i in range(366):
    if day[i] == 0:
        ans += cnt * deep
        cnt, deep = 0, 0
    else:
        cnt += 1 
        deep = max(day[i], deep)

# 365일이 0이 아니라면 ans에 값이 안더해지기 때문에 최종 더하기를 해야함.
ans += cnt * deep

print(ans)