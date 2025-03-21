"""
N,K = map(int(sys.stdin.readline().strip().strip())
1보다 크거나 같은 K
K보다 크거나 같은 N 입력으로 받음

1부터 N+1까지 range로 deque를 선언할 거임
그러면 1부터 N까지 deque에 저장되겠지

import sys
from collections import deque
N,K = map(int,(sys.stdin.readline().split()))
target = deque(range(1,K+1))
members = deque(range(1,N+1))
#i=0

def kill(N,K):
    i = 0
    while members:
        i += 1
        #if len(members) == 1:
        if len(members) == 1:   # members에 1명이 남아있으면
            return members.popleft()    #    popleft 하면서 그 번호를 return    
            #return members[0]
        else:   #members에 1명 이상 남아있으면
            #i += 1
            if i % K == 0:  # 그리고 만약 K번째가 되면
                members.popleft()   # 금마를 죽임
            else:   # K번째가 아니면
                target.popleft()
                index = (i + K) % len(members)  # 항상 현재 members 길이에 맞춰 안전한 인덱스
                target.append(members[index])
    kill(members,target)
    
print(kill(N,K))

처음에 이렇게 짰는데 인덱스 레인지를 자꾸 벗어남
"""



from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

# 1번부터 N번까지 사람을 deque에 넣는다
members = deque(range(1, N + 1))

def kill(members, K):
    result = []

    while members:
        # K가 3일 때 K-1 = 2, 즉 members의 앞사람을 뒤에 배치하는 행위를 두번 함
        for _ in range(K - 1):
            members.append(members.popleft())

        # 두번 그렇게 한 후에는 즉 세번째 차례니까 members의 맨 앞 사람을 없애고 result에 추가함
        result.append(members.popleft())

    return result

# 백준 요구 출력 형식에 맞춰서 출력
result = kill(members, K)
print("<" + ", ".join(map(str, result)) + ">")