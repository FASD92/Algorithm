def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 != 0:  # 만약 num_list[i]가 홀수면
            odd += str(num_list[i])
        else:   # 짝수면
            even += str(num_list[i])
    answer = int(odd) + int(even)
    return answer