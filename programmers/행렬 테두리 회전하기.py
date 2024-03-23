# Lv.2 행렬 테두리 회전하기

'''
문제
https://school.programmers.co.kr/learn/courses/30/lessons/77485

제한사항
rows는 2 이상 100 이하인 자연수입니다.
columns는 2 이상 100 이하인 자연수입니다.
처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
모든 회전은 순서대로 이루어집니다.
예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.
'''

def solution(rows, columns, queries):
    answer = []
    rect = []
    cnt = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp += [cnt]
            cnt += 1
        rect += [temp]
    
    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        cur = rect[x1][y1]
        mnum = cur
        for y in range(y1+1, y2+1):
            rect[x1][y], cur = cur, rect[x1][y]
            mnum = min(mnum, cur)
        
        for x in range(x1+1, x2+1):
            rect[x][y2], cur = cur, rect[x][y2]
            mnum = min(mnum, cur)

            
        for y in range(y2-1, y1-1, -1):
            rect[x2][y], cur = cur, rect[x2][y]
            mnum = min(mnum, cur)
            
        for x in range(x2-1, x1-1, -1):
            rect[x][y1], cur = cur, rect[x][y1]
            mnum = min(mnum, cur)
        
        answer += [mnum]
        # print(*rect, sep='\n')
        
    return answer