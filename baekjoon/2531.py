# 2531번 실버1 회전 초밥

'''
문제
https://www.acmicpc.net/problem/2531

입력
첫 번째 줄에는 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가 각각 하나의 빈 칸을 사이에 두고 주어진다. 단, 2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d이다. 두 번째 줄부터 N개의 줄에는 벨트의 한 위치부터 시작하여 회전 방향을 따라갈 때 초밥의 종류를 나타내는 1 이상 d 이하의 정수가 각 줄마다 하나씩 주어진다.

출력
주어진 회전 초밥 벨트에서 먹을 수 있는 초밥의 가짓수의 최댓값을 하나의 정수로 출력한다.

예제 입력 1 
8 30 4 30
7
9
7
30
2
7
9
25
예제 출력 1 
5
예제 입력 2 
8 50 4 7
2
7
9
25
7
9
7
30
예제 출력 2 
4

슬라이싱 윈도우
https://learning-e.tistory.com/36
초밥 숫자의 중복도 생각해야함
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

n,d,k,c = map(int, input().split())
plate = [int(input()) for _ in range(n)]
# 회전이기 때문에 연속되는 수 -1 만큼 뒤에도 추가
plate = plate + plate[:k]
# print(plate)
var = 0
# 쿠폰 스시 추가
window = defaultdict(int)
window[c] += 1
for i in range(k):
    window[plate[i]] += 1
    # print(window)

# 현재 0~3에서 시작한다면 0을 지우고 4를 더해야하기 때문
L,R = 0,k
for _ in range(n):
    var = max(var, len(window))
    window[plate[L]] -= 1
    # 종류가 사라진다면 딕셔너리에서 삭제
    if window[plate[L]] == 0:
        window.pop(plate[L])
    window[plate[R]] += 1
    L += 1
    R += 1

print(var)