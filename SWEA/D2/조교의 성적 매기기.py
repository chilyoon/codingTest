# 1983. 조교의 성적 매기기 D2

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=2

[제약사항]

1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)

2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)

3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.

테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
1
10 2
87 59 88
99 94 78
94 86 86
99 100 99
69 76 70
76 89 96
98 95 96
74 69 60
98 84 67
85 84 91

출력
#1 A-

'''

import sys
sys.stdin = open("../input.txt", "r")

# T = int(input())
#
# for t in range(1,T+1):
#     # N명의 학생 K번째의 학생 번호
#     N,K = map(int, input().split())
#     n = int(N/10)
#     grade = []
#     grade += ['A+']*n + ['A0']*n + ['A-']*n + ['B+']*n + ['B0']*n + ['B-']*n + ['C+']*n + ['C0']*n + ['C-']*n + ['D0']*n
#     # print(grade)
#     score = []
#     for i in range(N):
#         mid,final,task = map(int, input().split())
#         score.append((mid * 0.35) + (final * 0.45) + (task * 0.2))
#     rank = sorted(score,reverse=True)
#     # print(score)
#     # print(rank)
#     print(f'#{t} {grade[rank.index(score[K - 1])]}')

T = int(input())

for t in range(1,T+1):
    N,K = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score = []
    for i in range(N):
        mid,final,task = map(int, input().split())
        score.append((mid * 0.35) + (final * 0.45) + (task * 0.2))
    rank = sorted(score,reverse=True)
    print(f'#{t} {grade[rank.index(score[(K - 1)])//(N//10)]}')