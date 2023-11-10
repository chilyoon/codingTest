def solution(n, lost, reserve):
    answer = 0
    # lost와 reserve둘다 포함되면 나눠주지 못해 둘다 제거
    # lost가 삭제되며 문제 발생 [:]는 복사되며 오류가 안생김
    for i in lost[:]:
        # print ('lost i %d' % i)
        if i in reserve:
            # print ('reserve lost i %d' % i)
            reserve.remove(i)
            lost.remove(i)
    print(reserve,lost)
    # 1부터 n까지 반복 lost라면 양옆에 reserve가 있는지
    for i in range(1,n+1):
        # print('i %d' % i)
        if i in lost:
            for j in [i-1,i+1]:
                if j in reserve:
                    print('있음 %d' % j)
                    answer += 1
                    reserve.remove(j)
                    break
                else:
                    continue
        # lost가 아니라면 무조건 한벌은 가지고 있으니 +1 한다.
        else:
            answer += 1
    return answer
