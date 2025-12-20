"""
기존 코드 : 이렇게 하니까 RuntimeError: deque mutated during iteration 에러가 났다.
나뭇가지 위에 앉아 나뭇가지를 자르는 격이었다.

from collections import deque

def solution(s):
    
    circuits = []
    d = deque(s)
    
    for ch in d:
        left_char = d.popleft()
        
        if (len(circuits) != 0) and (left_char == ')' and circuits[-1] == '('):
            circuits.pop(-1)
        else:
            circuits.append(left_char)
    
    if not circuits:
        return False
    else:
        return True


"""

from collections import deque

def solution(s):
    circuits = []
    
    for ch in s:
        if circuits and (ch == ')' and circuits[-1] == '('):
            circuits.pop()
        else:
            circuits.append(ch)
            
    return len(circuits) == 0