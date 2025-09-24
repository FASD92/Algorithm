def solution(myString):
    parts = myString.split('x')
    result = []
    
    for ch in parts:
        if ch != '':
            result.append(ch)
            
    result.sort()
    return result