# 4659번 실버5 비밀번호 발음하기

'''
문제
https://www.acmicpc.net/problem/4659

입력
입력은 여러개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.

마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

출력
각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.

예제 입력 1 
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end
예제 출력 1 
<a> is acceptable.
<tv> is not acceptable.
<ptoui> is not acceptable.
<bontres> is not acceptable.
<zoggax> is not acceptable.
<wiinq> is not acceptable.
<eep> is acceptable.
<houctuh> is acceptable.
'''

while True:
    word = input()
    if word == 'end':
        break
    
    gather = ('a','e','i','o','u')
    cnt = 1
    pre = ''
    preGS = ''
    #자음g 모음s GS
    gs = ''
    f1,f2,f3 = False,True,True
    for i in word:
        if i in gather:
            f1 = True
            gs = 'g'
        else:
            gs = 's'

        if preGS == gs:
            cnt += 1
            if cnt >= 3:
                f2 = False
                # print(f'f2')
                break
        else:
            cnt = 1

        if pre == i and (pre != 'e' and pre != 'o'):
            f3 = False
            # print(f'f3 pre {pre} i {i}')
            break

        pre = i
        preGS = gs
    
    if f1 and f2 and f3:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
