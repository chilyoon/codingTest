# 10870번 브론즈2 파보나치 수 5

'''
문제
피보나치 수는 0과 1로 시작한다. 
0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. 
n은 20보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.

예제 입력 1 
10
예제 출력 1 
55
'''

import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
fibo = []
'''
for i in range(n+1):
    if i == 0:
        fibo[i] = 0
    elif i == 1:
        fibo[i] = 1
    else:
        fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])
'''
cnt = 0
def func(cnt):
    if cnt == n+1:
        print(fibo[n])
    else:
        if cnt == 0:
            fibo.append(0)
        elif cnt == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[cnt-1] + fibo[cnt-2])
        cnt += 1
        func(cnt)

func(cnt)
