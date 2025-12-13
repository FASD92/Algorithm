"""
numLog[i-1]과 numLog[i]의 차이를 int형 변수로 저장
해당 int형 변수를 키로 reversed_op에 값을 찾고
해당 값을 문자로 변환 후 answer에 추가함
"""

def solution(numLog):
    answer = ''
    op = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    reversed_op = {v: k for k, v in op.items()}
    diff_list = [numLog[i] - numLog[i-1] for i in range(1, len(numLog))]
    
    for key in diff_list:
        val = reversed_op[key]
        answer += str(val)
    
    return answer