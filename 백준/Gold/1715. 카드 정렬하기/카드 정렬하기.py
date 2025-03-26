import sys
import heapq

N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(N)]

if N == 1:
    print(0)
else:
    heapq.heapify(cards)
    answer = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        x = a + b
        answer += x
        heapq.heappush(cards, x)

    print(answer)