# 20444번 골드5 색종이와 가위

'''
문제
https://www.acmicpc.net/problem/20444

입력
첫 줄에 정수 n, k가 주어진다. (1 ≤ n ≤ 231-1, 1 ≤ k ≤ 263-1)

출력
첫 줄에 정확히 n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력한다.

예제 입력 1
4 9
예제 출력 1
YES


예제 입력 2
4 6
예제 출력 2
NO
4번의 가위질을 하는 모든 경우에 대해서 하나의 색종이를 6개의 색종이 조각으로는 만들 수 없다.

'''

import sys
input = sys.stdin.readline

# n번의 가위질로 k개의 색종이
n,k = map(int, input().split())

def binarySearch(left,right):
    while left <= right:
        mid = (left + right) // 2
        value = (mid + 1) * ((n-mid)+1)
        if value > k:
            right = mid - 1
        elif value < k:
            left = mid + 1
        else:
            print('YES')
            return
    print('NO')
    return

binarySearch(0,n//2)

# 시간 초과
# from collections import deque
#
# n,k = map(int, input().split())
# visit = set()
# queue = deque()
# # 가로 세로 자른 횟수
# queue.append((1,1,0))
#
# while queue:
#     x,y,cnt = queue.popleft()
#     hap = x * y
#     # print(x,y,cnt,hap)
#     if hap == k and cnt == n:
#         print('YES')
#         break
#     if cnt > n:
#         print('NO')
#         break
#     # print(cnt)
#     if (x+1)*y not in visit and (x+1)*y <= k:
#         queue.append((x+1,y,cnt+1))
#     if x*(y+1) not in visit and x*(y+1) <= k:
#         queue.append((x,y+1,cnt+1))