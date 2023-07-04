# 실버4 18258번 큐
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

queue = deque()

for _ in range(N):
    c = input().split()
    num = 0
    if(len(c) == 2):
        num = c[1]
    c = c[0]

    if(c == 'push'):
        queue.append(num)
    elif(c == 'pop'):
        if(len(queue) == 0):
            print('-1')
        else:
            print(queue[0])
            queue.popleft()
    elif(c == 'size'):
        print(len(queue))
    elif(c == 'empty'):
        print(0 if len(queue) else 1)
    elif(c == 'front'):
        if(len(queue) == 0):
            print('-1')
        else:
            print(queue[0])
    elif(c == 'back'):
        if(len(queue) == 0):
            print('-1')
        else:
            print(queue[-1])

    