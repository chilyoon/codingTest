import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs():
    if len(sequence) == M:
        # 이게 시간 더 빠름
        print(' '.join(map(str,sequence)))
        # print(*sequence)
        return
    
    for i in range(1,N+1):
            sequence.append(i)
            dfs()
            sequence.pop()

N,M = map(int, input().split())
sequence = []

dfs()