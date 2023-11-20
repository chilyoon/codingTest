# 21608번 골드5 상어 초등학교

'''
문제
https://www.acmicpc.net/problem/21608
입력
첫째 줄에 N이 주어진다. 둘째 줄부터 N2개의 줄에 학생의 번호와 그 학생이 좋아하는 학생 4명의 번호가 한 줄에 하나씩 선생님이 자리를 정할 순서대로 주어진다.

학생의 번호는 중복되지 않으며, 어떤 학생이 좋아하는 학생 4명은 모두 다른 학생으로 이루어져 있다. 입력으로 주어지는 학생의 번호, 좋아하는 학생의 번호는 N2보다 작거나 같은 자연수이다. 어떤 학생이 자기 자신을 좋아하는 경우는 없다.

출력
첫째 줄에 학생의 만족도의 총 합을 출력한다.

제한
3 ≤ N ≤ 20

예제 입력 1 
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4
예제 출력 1 
54

예제 입력 2 
3
4 2 5 1 7
2 1 9 4 5
5 8 1 4 3
1 2 9 3 4
7 2 3 4 8
9 8 4 5 7
6 5 2 3 4
8 4 9 2 1
3 9 2 1 4
예제 출력 2 
1053

'''

# 코드 정리
import sys
input = sys.stdin.readline

def check(llist):
    empty = -1
    good = -1
    xx, yy = 0,0
    for y in range(N):
        for x in range(N):
            if table[y][x] == 0:
                ecur = 0
                eempty = 0
                for ii in range(4):
                    nx = x + dx[ii]
                    ny = y + dy[ii]
                    if 0 <= nx < N and 0 <= ny < N:
                        if table[ny][nx] in llist:
                            ecur += 1
                        elif table[ny][nx] == 0:
                            eempty += 1
                if ecur == 4:
                    return [x,y]
                if ecur > good:
                    good = ecur
                    empty = eempty
                    xx = x
                    yy = y
                elif ecur == good and eempty > empty:
                    empty = eempty
                    xx = x
                    yy = y
    return [xx,yy]

N = int(input())
table = [[0]*N for _ in range(N)]
like = [list(map(int, input().split())) for _ in range(N**2)]
student = list(like[i].pop(0) for i in range(N**2))
table[1][1] = student[0]

dx,dy = [-1,1,0,0],[0,0,-1,1]

for i in range(1,N**2):
    result = check(like[i])
    table[result[1]][result[0]] = student[i]

answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        # 학생의 인덱스 
        idx = student.index(table[i][j])
        for ii in range(4):
            nx = j + dx[ii]
            ny = i + dy[ii]
            if 0 <= nx < N and 0 <= ny < N and table[ny][nx] in like[idx]:
                cnt += 1
        answer += int(10**(cnt-1))

print(answer)

# 문제 풀때 코드

# def check(llist):
#     empty = -1
#     good = -1
#     xx, yy = 0,0
#     for y in range(N):
#         for x in range(N):
#             if table[y][x] == 0:
#                 # print(f'x {x} y {y}')
#                 ecur = 0
#                 eempty = 0
#                 for ii in range(4):
#                     nx = x + dx[ii]
#                     ny = y + dy[ii]
#                     # print(f'nx {nx} ny {ny}')
#                     if 0 <= nx < N and 0 <= ny < N and table[ny][nx] in llist:
#                         ecur += 1
#                     if 0 <= nx < N and 0 <= ny < N and table[ny][nx] == 0:
#                         eempty += 1
#                 # print(ecur, eempty)
#                 if ecur == 4:
#                     return [x,y]
#                 if ecur > good:
#                     # print('ecur > good')
#                     # print(f'e {empty} ee {eempty} g {good} ec {ecur}')
#                     good = ecur
#                     empty = eempty
#                     # print(f'e {empty} ee {eempty} g {good} ec {ecur}')
#                     xx = x
#                     yy = y
#                 elif ecur == good and eempty > empty:
#                     # print('ecur == good and eempty > empty')
#                     # print(f'e {empty} ee {eempty} g {good} ec {ecur}')
#                     empty = eempty
#                     # print(f'e {empty} ee {eempty} g {good} ec {ecur}')
#                     xx = x
#                     yy = y
#     return [xx,yy]

# # def empty():
# #     cnt = 0
# #     xx, yy = 0,0
# #     for y in range(N):
# #         for x in range(N):
# #             if table[y][x] == 0:
# #                 cur = 0
# #                 for ii in range(4):
# #                     nx = x + dx[ii]
# #                     ny = y + dy[ii]
# #                     if 0 <= nx < N and 0 <= ny < N and table[ny][nx] != 0:
# #                         cur += 1
# #                 if cur == 4:
# #                     return [x,y]
# #                 if cur > cnt:
# #                     cnt = cur
# #                     xx = x
# #                     yy = y
# #     return [xx,yy]

# N = int(input())
# table = [[0]*N for _ in range(N)]
# like = [list(map(int, input().split())) for _ in range(N**2)]
# student = list(like[i].pop(0) for i in range(N**2))
# table[1][1] = student[0]

# dx,dy = [-1,1,0,0],[0,0,-1,1]

# for i in range(1,N**2):
#     # print(f'student : {student[i]}')
#     flag = True
#     # for j in student[:i]:
#     result = check(like[i])
#     # print(result)
#     table[result[1]][result[0]] = student[i]
#     # print(*table, sep='\n')
#     #     if j in like[i]:
#     #         print('좋아함')
#     #         result = check(like[i])
#     #         print(result)
#     #         table[result[1]][result[0]] = student[i]
#     #         flag = False
#     #         break
#     # if flag:
#     #     print('없네')
#     #     result = empty()
#     #     print(result)
#     #     table[result[1]][result[0]] = student[i]
#     # print(*table,sep='\n')

# # print(*table,sep='\n')

# answer = 0
# for i in range(N):
#     for j in range(N):
#         cnt = 0
#         # 학생의 인덱스 
#         idx = student.index(table[i][j])
#         for ii in range(4):
#             nx = j + dx[ii]
#             ny = i + dy[ii]
#             if 0 <= nx < N and 0 <= ny < N and table[ny][nx] in like[idx]:
#                 cnt += 1
#         answer += int(10**(cnt-1))

# print(answer)