def solution(ineq, eq, n, m):
    if eq == "=":
        result = (n <= m) if ineq == '<' else (n >= m)
    else:
        result = (n < m) if ineq == '<' else (n > m)
    return int(result)  # True -> 1, False -> 0 자동 변환되기 때문
    
    
"""
아래는 리팩터링 전 코드

def solution(ineq, eq, n, m):
    answer = 0
    if ineq == '<':
        if eq == '=':
            if n <= m:
                answer = 1
            else:
                answer = 0
        else:
            if n < m:
                answer = 1
            else:
                answer = 0
    else:
        if eq == '=':
            if n >= m:
                answer = 1
            else:
                answer = 0
        else:
            if n > m:
                answer = 1
            else:
                answer = 0
    return answer
"""