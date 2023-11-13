# 1928. Base64 Decoder D2

'''
문제
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PR4DKAG0DFAUq&categoryId=AV5PR4DKAG0DFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
[제약사항]
문자열의 길이는 항상 4의 배수로 주어진다.
그리고 문자열의 길이는 100000을 넘지 않는다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

입력
5
TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u
U3VzcGljaW9uIGZvbGxvd3MgY2xvc2Ugb24gbWlzdHJ1c3Qu
VG8gZG91YnQgaXMgc2FmZXIgdGhhbiB0byBiZSBzZWN1cmUu
T25seSB0aGUganVzdCBtYW4gZW5qb3lzIHBlYWNlIG9mIG1pbmQu
QSBmdWxsIGJlbGx5IGlzIHRoZSBtb3RoZXIgb2YgYWxsIGV2aWwu

출력
#1 Life itself is a quotation.
#2 Suspicion follows close on mistrust.
#3 To doubt is safer than to be secure.
#4 Only the just man enjoys peace of mind.
#5 A full belly is the mother of all evil.

'''

import sys
sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

from base64 import b64decode

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {b64decode(input()).decode("UTF-8")}')