# 8979번 실버5 올림픽

'''
문제
https://www.acmicpc.net/problem/8979

입력
입력의 첫 줄은 국가의 수 N(1 ≤ N ≤ 1,000)과 등수를 알고 싶은 국가 K(1 ≤ K ≤ N)가 빈칸을 사이에 두고 주어진다. 각 국가는 1부터 N 사이의 정수로 표현된다. 이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 이 국가가 얻은 금, 은, 동메달의 수가 빈칸을 사이에 두고 주어진다. 전체 메달 수의 총합은 1,000,000 이하이다.

출력
출력은 단 한 줄이며, 입력받은 국가 K의 등수를 하나의 정수로 출력한다. 등수는 반드시 문제에서 정의된 방식을 따라야 한다. 

서브태스크
번호	배점	제한
1	8	
예제 입력, 출력

2	12	
N = 2

3	20	
모든 국가의 은메달 및 동메달 획득 수는 0

4	25	
N ≤ 500

5	35	
추가적인 제약 조건은 없다.

예제 입력 1 
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
예제 출력 1 
2
예제 입력 2 
4 2
1 3 0 0
3 0 0 2
4 0 2 0
2 0 2 0
예제 출력 2 
2
'''

import sys
input = sys.stdin.readline

# 국가의 수 n 등수를 알고 싶은 국가 k
n,k = map(int, input().split())
# medal = [list(map(int,input().split())) for _ in range(n)]
medal = []
idx = 0
for j in range(n):
    i,g,s,b = map(int, input().split())
    if i == k:
        idx = j
    medal += [[i,g,s,b]]

rank = 1
for i in range(n):
    if medal[i][1] > medal[idx][1]:
        rank += 1
    elif medal[i][1] == medal[idx][1]:
        if medal[i][2] > medal[idx][2]:
            rank += 1
        elif medal[i][2] == medal[idx][2] and medal[i][3] > medal[idx][3]:
                rank += 1

print(rank)