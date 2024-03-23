# Lv.1 로또의 최고 순위와 최저 순위

'''
문제
https://school.programmers.co.kr/learn/courses/30/lessons/77484

제한사항
lottos는 길이 6인 정수 배열입니다.
lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
0은 알아볼 수 없는 숫자를 의미합니다.
0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
win_nums은 길이 6인 정수 배열입니다.
win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.
'''

def solution(lottos, win_nums):
    answer = []
    lotto = [6,6,5,4,3,2,1]
    cnt,rank = 0,0
    for i in lottos:
        if i == 0:
            cnt += 1
            continue
        else:
            for j in win_nums:
                if i == j:
                    rank += 1
    answer += [lotto[rank+cnt], lotto[rank]]
    return answer