"""
체육 수업을 들을 수 있는 학생의 최댓값을 return

간단하게
i가 1일 때는 lost[i+1]이 reserve에 존재하는지 확인하고 없으면 count--
i > 1 일 때는 lost[i-1] 또는 lost[i+1]이 reserve에 존재하는지 확인하고 없으면 count --

기존 코드 : 이렇게 하니 인덱스 에러가 떴다. 일단 for i in lost에서 i는 잃어버린 학생의 번호(값)이 되기 때문에 인덱스를 벗어나는 에러가 나는 것.

def solution(n, lost, reserve):
    answer = 0
    count = n
    
    for i in lost:
        if len(lost) >= 2: 
            if i == 1:
                if lost[i+1] in reserve:
                    count -= 1
            elif i > 1:
                if not (lost[i-1] or lost[i+1] in reserve):
                    count -= 1
    answer = count
    return answer

"""

def solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for student in sorted(real_lost):
        if student - 1 in real_reserve:
            real_reserve.remove(student - 1)
        elif student + 1 in real_reserve:
            real_reserve.remove(student + 1)
        else:
            n -= 1
        
    return n