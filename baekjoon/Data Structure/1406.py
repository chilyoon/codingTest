# 1406번 실버2 에디터

'''
문제
https://www.acmicpc.net/problem/1406

입력
첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

출력
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.

예제 입력 1 
abcd
3
P x
L
P y
예제 출력 1 
abcdyx
예제 입력 2 
abc
9
L
L
L
L
L
P x
L
B
P y
예제 출력 2 
yxabc
예제 입력 3 
dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z
예제 출력 3 
yxz

--> 시간초과 문자열의 최대 길이는 60만이므로 커서에 따라 리스트를 수정하는 방식은 시간 복잡도가 높아 시간 초과가 발생
연결리스트와 스택을 활용한 자료구조 문제 풀이
'''
import sys
input = sys.stdin.readline
from collections import deque

Lword = list(input().rstrip())
Rword = deque()

t = int(input())
for i in range(t):
    com = input().split()
    if com[0] == "L" and Lword:
        Rword.appendleft(Lword.pop())
    elif com[0] == "D" and Rword:
        Lword.append(Rword.popleft())
    elif com[0] == "B" and Lword:
        Lword.pop()
    elif com[0] == "P":
        Lword.append(com[1])

    # print(Lword)
    # print(Rword)

for i in range(len(Lword)):
    print(Lword[i], end="")
for i in range(len(Rword)):
    print(Rword[i], end="")

'''
# 시간초과 문자열의 최대 길이는 60만이므로 커서에 따라 리스트를 수정하는 방식은 시간 복잡도가 높아 시간 초과가 발생
# word = list(input().rstrip())

# n = len(word)
# cur = n
# t = int(input())
# com = [input().rstrip() for _ in range(t)]

# for i in range(t):
#     if len(com[i]) == 1:
#         if com[i] == "L" and cur != 0:
#             cur -= 1
#         elif com[i] == "D" and cur != (n+1):
#             cur += 1
#         elif com[i] == "B" and cur != 0:
#             word = word[:cur-1] + word[cur:]
#             n -= 1
#             cur -= 1
#     else:
#         c,w = com[i].split()
#         word = word[:cur] + [w] + word[cur:]
#         n += 1
#         cur += 1
    
# print(*word)
'''