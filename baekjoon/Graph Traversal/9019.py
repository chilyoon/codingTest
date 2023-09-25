# 9019번 골드4 DSLR

'''
문제
https://www.acmicpc.net/problem/9019
입력
프로그램 입력은 T 개의 테스트 케이스로 구성된다. 테스트 케이스 개수 T 는 입력의 첫 줄에 주어진다. 각 테스트 케이스로는 두 개의 정수 A와 B(A ≠ B)가 공백으로 분리되어 차례로 주어지는데 A는 레지스터의 초기 값을 나타내고 B는 최종 값을 나타낸다. A 와 B는 모두 0 이상 10,000 미만이다.

출력
A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력한다. 가능한 명령어 나열이 여러가지면, 아무거나 출력한다.

예제 입력 1 
3
1234 3412
1000 1
1 16
예제 출력 1 
LL
L
DDDD
'''

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
'''
D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
'''
def D(a):
    n = a*2
    if n >= 10000:
        return n%10000
    else:
        return n

def S(a):
    n = a-1
    if n == -1:
        return 9999
    else:
        return n

def L(a):
    d1 = a//1000
    d2 = (a%1000)//100
    d3 = (a%100)//10
    d4 = a%10
    return (d2*1000) + (d3*100) + (d4*10) + d1

def R(a):
    d1 = a//1000
    d2 = (a%1000)//100
    d3 = (a%100)//10
    d4 = a%10
    return (d4*1000) + (d1*100) + (d2*10) + d3

def bfs(B):
    visit = set()
    while queue:
        a,command = queue.popleft()
        if a == B:
            return command
        else:
            d = D(a)
            # print(d)
            if d not in visit:
                visit.add(d)
                queue.append((d,command+"D"))
            s = S(a)
            # print(s)
            if s not in visit:
                visit.add(s)
                queue.append((s,command+"S"))
            l = L(a)
            # print(l)
            if l not in visit:
                visit.add(l)
                queue.append((l,command+"L"))
            r = R(a)
            # print(r)
            if r not in visit:
                visit.add(r)
                queue.append((r,command+"R"))
            
            
for _ in range(T):
    A,B = map(int, input().split())
    queue = deque([(A,"")])
    print(bfs(B))