"""
DFS로 모든 경우의 수를 찾아야 할 것 같다.
numbers[i]가 주어지면, +numbers[i], -numbers[i] 두 갈림길로 나뉘어야 할 것 같은데..
이걸 어떻게 visited를 처리하지?
결국 시간 안에 풀지 못했다
"""

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx, current_sum):
        nonlocal answer
        
        if idx == n:
            if current_sum == target:
                answer += 1
            return
        
        dfs(idx + 1, current_sum + numbers[idx])
        dfs(idx + 1, current_sum - numbers[idx])
        
    dfs(0, 0)    
    return answer