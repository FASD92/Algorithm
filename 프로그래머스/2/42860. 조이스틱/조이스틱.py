"""
ASCII
A = 65
Z = 90

맨 처음 A로 시작한다는 가정하에

A부터 N까지는 조이스틱을 위로 입력
O부터 Z까지는 조이스틱을 아래로 입력하는 게 유리함 -> ((ord('O') - 65) - ord('O)) + 1

기존 코드

def solution(name):
    answer = 0
    
    # 문자열 길이가 3일 경우에 대한 예외처리... 인데 이렇게 하면 O부터 Z까지의 문자에 대한 예외처리는 또 어떻게 하지?
    if len(name) == 3 and name[1] == 'A':
        return (ord(name[0]) - 65) + 1 + (ord(name[2]) - 65)
    
    for ch in name:
        if ord(ch) - 65 <= 13:
            
            
        
    return answer
    
"""

def solution(name):
    n = len(name)
    answer = 0
    min_move = n - 1    # 기본은 오른쪽 끝까지 이동
    
    for i, ch in enumerate(name):
        answer += (min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)) # 상하 이동 합산
        
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        min_move = min([min_move, i + n - next_idx + min(i, n- next_idx)])
        
    return answer + min_move