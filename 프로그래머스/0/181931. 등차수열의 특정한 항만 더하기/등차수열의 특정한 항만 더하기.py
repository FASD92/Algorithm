def solution(a, d, included):
    result = 0
    
    for i in range(len(included)):
        if included[i] == True:
            result += a + d * i
                
    return result