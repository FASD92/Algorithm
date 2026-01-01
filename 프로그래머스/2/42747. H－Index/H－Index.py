"""
논문의 인용 횟수를 담은 배열 citatitons

"""


def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            answer = i + 1
        else:
            break
            
    return answer