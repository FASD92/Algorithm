"""
주어진 배열을 재정렬 해야 하나? 해야 한다면 어떻게?
DFS를 사용해야 하나?
DFS를 사용하면서 푸는 도중 시간 안에 풀지 못함

기존 코드 : 
def solution(clothes):
    answer = 0
    n = len(clothes)
    wore = [False] * n
    
    def dfs(clothes, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n):
            if not wore[i]:
                wore[i] = True
                dfs()
    
    return answer

"""
def solution(clothes):
    answer = 1
    closet = {}

    for name, kind in clothes:
        if kind in closet:
            closet[kind] += 1
        else:
            closet[kind] = 1
            
    for count in closet.values():
        answer *= (count + 1)

    return answer - 1