import sys
import heapq

N = int(sys.stdin.readline().strip())
max_hq = []
min_hq = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())

    if not max_hq or num <= -max_hq[0]:
        heapq.heappush(max_hq, -num)
    else:
        heapq.heappush(min_hq, num)

    if len(max_hq) > len(min_hq) + 1:
        heapq.heappush(min_hq, -heapq.heappop(max_hq))
    elif len(min_hq) > len(max_hq):
        heapq.heappush(max_hq, -heapq.heappop(min_hq))

    print(-max_hq[0])