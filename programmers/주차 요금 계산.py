# Lv.2 주차 요금 계산

'''
문제
https://school.programmers.co.kr/learn/courses/30/lessons/92341
입출력 예
fees	records	result
[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.

입출력 예 #2

요금표
기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
120	0	60	591


입/출차 기록
시각(시:분)	차량 번호	내역
16:00	3961	입차
16:00	0202	입차
18:00	3961	출차
18:00	0202	출차
23:58	3961	입차


자동차별 주차 요금
차량 번호	누적 주차 시간(분)	주차 요금(원)
0202	120	0
3961	120 + 1 = 121	0 +⌈(121 - 120) / 60⌉x 591 = 591
3961번 차량은 2번째 입차된 후에는 출차된 내역이 없으므로, 23:59에 출차되었다고 간주합니다.


입출력 예 #3

요금표
기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
1	461	1	10


입/출차 기록
시각(시:분)	차량 번호	내역
00:00	1234	입차


자동차별 주차 요금
차량 번호	누적 주차 시간(분)	주차 요금(원)
1234	1439	461 +⌈(1439 - 1) / 1⌉x 10 = 14841
1234번 차량은 출차 내역이 없으므로, 23:59에 출차되었다고 간주합니다.

'''

from math import ceil
from collections import defaultdict


def solution(fees, records):
    answer = []
    num, time = [], []
    pay = defaultdict(int)
    for i in records:
        l = i.split()
        if l[2] == 'IN':
            num += [l[1]]
            time += [int(l[0][:2]) * 60 + int(l[0][3:])]
        else:
            idx = num.index(l[1])
            out_t = int(l[0][:2]) * 60 + int(l[0][3:])
            out_t -= time[idx]
            pay[l[1]] += out_t
            num.remove(num[idx])
            time.remove(time[idx])
    while num:
        last = 23 * 60 + 59
        pay[num[0]] += last - time[0]
        num.pop(0)
        time.pop(0)

    for k, v in pay.items():
        fee = fees[1]
        if v > fees[0]:
            fee += (ceil((v - fees[0]) / fees[2])) * fees[3]
        pay[k] = fee

    pay = sorted(list([k, v] for k, v in pay.items()))

    for i in pay:
        answer += [i[1]]
    return answer