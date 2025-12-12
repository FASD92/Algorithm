def solution(num_list):
    multipled = 1
    answer = 0
    for i in range(len(num_list)):
        multipled *= num_list[i]
        
    if (sum(num_list) ** 2) > multipled:
        answer = 1
    else:
        answer = 0
        
    return answer