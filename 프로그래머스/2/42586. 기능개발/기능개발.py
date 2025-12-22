"""
for 루프를 돌며 모든 progresses의 원소에 대응되는 speeds의 원소의 값을 더해야 한다.
if progresses[0]의 값이 100보다 크거나 같아지면

또 다른 for 루프를 돌며 i+=1, count += 1을 한다.
언제까지? 100보다 작은 원소를 찾을 때까지.
이 때의 i를 answer.append(i)로 더하자.
근데 이렇게 하면 또 index out of range 뜨는 것 아닌가...? 아니면 잘못된 값이 나온다거나

결국 시간 안에 못풀었음
수식을 만들었으면 금방 만들었을텐데
아래는 기존 코드

def solution(progresses, speeds):
    answer = []
    pointer = 0 # 배포일의 기준이 되는 포인터
    while progresses:   # 모든 기능이 배포될 때까지
        for i in range(len(progresses)):    # progresses를 순회하면서
            progresses[i] += speeds[i]  # 개발 속도를 진도에 더함
            if progresses[pointer] >= 100:    # 만약 배포해야 할 기능을 찾으면
                for j in range(pointer, len(progresses)):    # 배포해야 하는 기능부터 순회하면서
                    if progresses[j] < 100: # 아직 배포 안된 기능을 만나면
                        answer.append(j + 1)    # 0-인덱스니까 j + 1을 해주고
                        break   # for문을 나온다.
    return answer
"""

import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        required_day = math.ceil((100 - p) / s)
        days.append(required_day)
        
    max_day = days[0]
    count = 0
    
    for day in days:
        if day <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = day
            count = 1
    
    answer.append(count)
    return answer