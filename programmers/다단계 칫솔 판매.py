# Lv.3 다단계 칫솔 판매

'''
문제
https://school.programmers.co.kr/learn/courses/30/lessons/77486

제한사항
enroll의 길이는 1 이상 10,000 이하입니다.
enroll에 민호의 이름은 없습니다. 따라서 enroll의 길이는 민호를 제외한 조직 구성원의 총 수입니다.
referral의 길이는 enroll의 길이와 같습니다.
referral 내에서 i 번째에 있는 이름은 배열 enroll 내에서 i 번째에 있는 판매원을 조직에 참여시킨 사람의 이름입니다.
어느 누구의 추천도 없이 조직에 참여한 사람에 대해서는 referral 배열 내에 추천인의 이름이 기입되지 않고 “-“ 가 기입됩니다. 위 예제에서는 john 과 mary 가 이러한 예에 해당합니다.
enroll 에 등장하는 이름은 조직에 참여한 순서에 따릅니다.
즉, 어느 판매원의 이름이 enroll 의 i 번째에 등장한다면, 이 판매원을 조직에 참여시킨 사람의 이름, 즉 referral 의 i 번째 원소는 이미 배열 enroll 의 j 번째 (j < i) 에 등장했음이 보장됩니다.
seller의 길이는 1 이상 100,000 이하입니다.
seller 내의 i 번째에 있는 이름은 i 번째 판매 집계 데이터가 어느 판매원에 의한 것인지를 나타냅니다.
seller 에는 같은 이름이 중복해서 들어있을 수 있습니다.
amount의 길이는 seller의 길이와 같습니다.
amount 내의 i 번째에 있는 수는 i 번째 판매 집계 데이터의 판매량을 나타냅니다.
판매량의 범위, 즉 amount 의 원소들의 범위는 1 이상 100 이하인 자연수입니다.
칫솔 한 개를 판매하여 얻어지는 이익은 100 원으로 정해져 있습니다.
모든 조직 구성원들의 이름은 10 글자 이내의 영문 알파벳 소문자들로만 이루어져 있습니다.
'''

from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = []
    recommend = defaultdict()
    money = defaultdict(int)
    
    for i in range(len(enroll)):
        recommend[enroll[i]] = referral[i]
        money[enroll[i]] = 0
    
    for i in range(len(seller)):
        cur = seller[i]
        curMoney = amount[i]*100
        money[cur] += (amount[i]*100)
        
        while recommend[cur] != "-":
            if curMoney == 0:
                break
            curMoney = int(0.1*curMoney)
            money[cur] -= curMoney
            cur = recommend[cur]
            money[cur] += curMoney
            
        if recommend[cur] == "-":
            money[cur] -= int(0.1*curMoney)
    
    for i in enroll:
        answer += [money[i]]
    
    return answer