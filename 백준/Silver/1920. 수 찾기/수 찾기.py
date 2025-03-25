"""
첫번째 줄 정수 A의 개수 N
두번째 줄 N개의 리스트 arr
세번째 줄 정수 M의 개수 M
네번재 줄 M개의 리스트 nums

정수 A의 개수를 int형 변수 N으로 선언
두번째 줄을 리스트 arr를 int형으로 맵핑해서 리스트로 만듦
그리고 arr를 .sort()로 정렬
세번째 줄 정수 M의 개수를 int형 변수 M을 선언
네번째 줄을 int형으로 맵핑해서 리스트로 만듦 리스트명은 nums

nums의 항목을 하나씩 arr에 있는지 bisect_left로 검사함
그러면, 그 항목이 arr에 있다면, idx 변수에 그 항목이 저장될텐데
만약 arr에 없는 걸 bisect_left 하면 N을 벗어난 값을 저장할 수도 있으니
(배열의 맨 끝을 가리킬 수 있으니)
idx < N이면서 arr[idx]가 nums[i]와 일치하다면 1을,
아니면 0을 출력함
"""
import sys
from bisect import bisect_left

N = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

M = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M):
    idx = bisect_left(arr, nums[i])
    if idx < N and arr[idx] == nums[i]:
        print(1)
    else:
        print(0)