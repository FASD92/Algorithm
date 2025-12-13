"""
queries의 원소에서 s,e,k를 추출
s <= arr[i] <= e 이면서 min(arr[i] > k)
result에 append
"""

def solution(arr, queries):
    result = []
    for s, e, k in queries:
        candidates = []
        for i in range(len(arr)):
            if s <= i <= e and arr[i] > k:
                candidates.append(arr[i])
        if len(candidates) == 0:
            candidates.append(-1)
        result.append(min(candidates))
    return result