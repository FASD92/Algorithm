"""
전깃줄 개수 N

일단 전깃줄 A-B 연결 정보를 튜플로 리스트 저장함 -> list = []
이 때 정렬은 A 오름차순
그리고 정렬된 튜플 순 그대로 B만의 리스트를 만듦 bar_b = []
dp를 저장할

그러면 그 리스트로 LIS를 만들 수 있을텐데...
반복문 또는 이진탐색, bisect로 가능함
근데 이진탐색 기억이 잘 안 나니까... 반복문으로?

아무튼 LIS가 나오면 N - LIS를 저장해서 출력함
"""
import sys

N = int(sys.stdin.readline().strip())
list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
#print(list)
list.sort()

bar_b = [b for a, b in list]
#print(bar_b)
dp = [1] * N

for i in range(N):
    for j in range(i):
        if bar_b[j] < bar_b[i]:
            dp[i] = max(dp[i], (dp[j] + 1))

print(N - (max(dp)))
#print(max(dp))