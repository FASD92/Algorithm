"""
상근이가 갖고 있는 숫자 카드 N개
숫자 카드 리스트는 arr

찾아야 할 숫자 리스트 M개
찾아야 할 숫자 리스트는 nums

이분 탐색해야 하니 arr는 .sort
bisect_left로 찾고 그 인덱스를 idx에 저장함

M개를 하나씩 뽑아서 arr와 비교하는 반복문
만약 idx가 N개의 개수보다 작고(arr 안에 nums[i])가 없어서 인덱스 레인지를 벗어나는 걸 방지)
그 인덱스에 해당하는 arr의 값과 현재 뽑은 M의 값이 같다면 1출력
아니면 0 출력


"""

import sys
from bisect import bisect_left

N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

M = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))
result = []

for i in range(M):
    idx = bisect_left(arr, nums[i])
    if idx < N and arr[idx] == nums[i]:
        result.append(1)
    else:
        result.append(0)

print(*result)