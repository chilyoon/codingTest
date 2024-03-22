# 7568번 실버5 덩치

'''
문제
https://www.acmicpc.net/problem/7568

입력
첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

출력
여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.

제한
2 ≤ N ≤ 50
10 ≤ x, y ≤ 200
예제 입력 1 
5
55 185
58 183
88 186
60 175
46 155
예제 출력 1 
2 2 1 2 5
'''

# import sys
# input = sys.stdin.readline

# n = int(input())
# human = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     cnt = 1
#     for j in range(n):
#         if human[j][0] > human[i][0] and human[j][1] > human[i][1]:
#             cnt += 1
#     print(cnt, end=' ')


import sys
input = sys.stdin.readline

n = int(input())
human = []
for i in range(n):
    # x 몸무게 y 키
    x,y = map(int, input().split())
    human += [[i,x,y]]

human.sort(key = lambda x : (x[2],x[1]), reverse=True)
print(human)
rank,cnt = 1,1
for i in range(n-1):
    human[i] += [rank]

    if human[i][2] > human[i+1][2] and human[i][1] > human[i+1][1]:
        rank += cnt
        cnt = 1
    else:
        cnt += 1

human[-1] += [rank]

human.sort()
print(human)
for i in range(n):
    print(human[i][-1], end=' ')
