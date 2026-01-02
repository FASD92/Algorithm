def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for h in range(3, int(total ** 0.5) + 1):
        if total % h == 0:
            w = total // h
            
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
    
    return answer