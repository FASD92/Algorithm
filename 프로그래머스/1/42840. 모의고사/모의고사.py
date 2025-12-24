def solution(answers):
#    soopo_1 = [1, 2, 3, 4, 5]
#    soopo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
#    soopo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    soopo = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    scores = [0, 0, 0]
    
    for i in range(len(soopo)):
        
        current_pattern = soopo[i]
        
        for j in range(len(answers)):
            if answers[j] == current_pattern[j % len(current_pattern)]:
                scores[i] += 1
                
    max_scores = max(scores)
    result = []
    
    for i in range(len(scores)):
        if scores[i] == max_scores:
            result.append(i + 1)
    
    return result