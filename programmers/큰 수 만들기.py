# Lv.2 큰 수 만들기

'''
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
'''

'''
스택 활용하기, while문 잘 활용하기
'''

def solution(number, k):
    stack = []
    for n in number:
        while len(stack)>0 and k>0 and stack[-1]<n:
            stack.pop()
            k -= 1
        stack.append(n)
    if k:
        return number[:-k]
    else:
        return "".join(stack)

    
#     시간 초과 코드
#     answer = ''    
#     num = list(number)
#     s = 0

#     while k > 0:
#         flag = True

#         for i in range(s,len(num)-1):
#             if num[i] == '9':
#                 s = i
#             elif num[i] < num[i+1]:
#                 num.pop(i)
#                 k -= 1
#                 flag = False
#                 break
#         if flag:
#             break
    
#     if k == 0:
#         return ''.join(num)
#     else:
#         return ''.join(num[:-k])
    

