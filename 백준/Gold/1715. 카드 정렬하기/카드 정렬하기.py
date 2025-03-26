"""
카드 '묶음'의 개수 N -> int
카드 묶음의 크기를 담은 리스트 -> int형으로 맵핑
비교 횟수를 저장할 x -> int

N이 1, 즉 카드가 1개일 때는 비교할 대상이 없으므로 1을 출력

N이 1이 아니면, 즉 1보다 크면
cards를 최소힙 구조로 바꾸고

힙에 카드 묶음이 2개 이상 남아있는 동안 반복
=> 2개 이상 남아있어야 두 묶음을 합칠 수 있으니까...!
누적합 result = 0으로 초기화

cards에서 heappop으로 하나 뽑고
한번 더 뽑고 두 카드를 더해 x에 저장하고

result = result + x 로 누적합을 만듦
그리고 가장 작은 카드 두개의 합이었던 x를 다시 cards에 heappush함
"""
import sys
import heapq

N = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(N)]

if N == 1:
    print(0)
else:
    heapq.heapify(cards)
    result = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        x = a + b
        result += x
        heapq.heappush(cards, x)

    print(result)
