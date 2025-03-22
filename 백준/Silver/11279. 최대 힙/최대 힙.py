"""
배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

최대힙을 구하는 거니까 음수를 붙여 저장하고, 음수를 붙여 출력해야겠다.
heappush와 heappop은 동작을 하면서 힙을 유지시키는 메서드니까!
"""
import sys
import heapq

input = sys.stdin.readline
N = int(input().strip())
heap_arr = []
i=0

while i<N:
    num = int(input().strip())
    if num > 0:
        heapq.heappush(heap_arr,-num)
    else:
        if not heap_arr:
            print(0)
        else:
            print(-heapq.heappop(heap_arr))
    i+=1