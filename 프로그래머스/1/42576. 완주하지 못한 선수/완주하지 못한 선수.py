"""
배열 participant
배열 completion

단 한 명의 선수를 제외하고는 모든 참가자가 마라톤을 완주했다.
동명이인이 있을 수 있다.
완주하지 못한 선수의 이름을 return

만약 두 배열을 합쳐서 set으로 중복을 모두 없앤다면?
동명이인까지 사라져버리니 이 방법은 안 됨...

예를 들어
leo kiki leo(동명이인)가 참여해서
leo kiki가 완주했다면 
leo만 리턴해야 하는 건데...

저 두 배열을 합치면,
leo kiki leo leo kiki
set으로 중복을 제거하면
leo kiki

간단하게 이 문제는
completion에는 있고
participant에는 없는 값을 찾는 것

더 간단하게 설명하자면
두 배열을 앞에서부터 가리키는 포인터 두 개
그 포인터를 하나씩 한 칸씩 옮기며 값을 비교하다가
completion을 기준으로 값이 다른 걸 출력하면 되는 것


기존 코드

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if i < len(completion) and participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            answer = participant[-1]
    return answer
    

근데 이렇게 하니까 참가자가 1명일 때 케이스를 커버할 수 없었음

"""
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 만약 알파벳 순서대로 정렬했는데 서로 다른 값이 나오면 그 놈이 정답
            return participant[i]
        
    return participant[-1]  # 만약 다 비교했는데도 없으면 맨 마지막 놈이 정답. 또는 참가자가 1명일 때도 그 놈이 정답.