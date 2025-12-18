"""
i, j, k

for문에서 2차원 배열의 원소를 순회할 때마다 초기화될 수 있는 배열을 만들어야 할 거 같은데...

"""

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced = array[i-1:j]
        sorted_sliced = sorted(sliced)
        picked = sorted_sliced[k-1]
        answer.append(picked)
    return answer