# 1987번 골드4 알파벳

'''
문제
https://www.acmicpc.net/problem/1987
입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력 1 
2 4
CAAB
ADCB
예제 출력 1 
3
예제 입력 2 
3 6
HFDFFB
AJHGDH
DGAGEH
예제 출력 2 
6
예제 입력 3 
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
예제 출력 3 
10
'''

import sys
input = sys.stdin.readline

def dfs(cnt, x, y):
    # print('cnt %d x %d y %d Alpha %s' % (cnt,x,y,board[y][x]))
    # 알파벳은 26개가 최대이기 때문에 26개가 되는순간 출력하고 종료
    if cnt == 26:
        print(26)
        sys.exit()
    deep.add(cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in visit:
            visit.add(board[ny][nx])
            dfs(cnt+1, nx, ny)
            visit.remove(board[ny][nx])

# 세로 R 가로 C
R,C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
visit = set(board[0][0])
deep = set()
dx,dy = [-1,1,0,0],[0,0,-1,1]

dfs(1,0,0)
print(max(deep))