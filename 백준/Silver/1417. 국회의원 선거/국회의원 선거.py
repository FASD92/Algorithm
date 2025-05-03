"""
다솜이가 기호 1번
국회의원 후보는 N명
주민 M명

다솜이 girl이니까 readline으로 읽어들여서 int형으로 저장
heap = []
first = 0
count = 0
heap에는 최대힙이니까 음수 붙여서 저장
vote = sys.readline...


heappop해서 저장할 현재 1등 후보 first

반복문은 다솜이가 first보다 커질 때까지
    heappop해서 first에 저장하고
    다솜이 += 1
    first -= 1
    count += 1

반복문 빠져나오면 print(count)
"""
import sys
import heapq

N = int(sys.stdin.readline().strip())
#print(N)
girl = int(sys.stdin.readline().strip())
count = 0
#print(girl)

heap = []

for _ in range(N-1):
    vote = int(sys.stdin.readline().strip())
    heapq.heappush(heap, -vote)
#print(heap)

while heap:
    first = -heapq.heappop(heap)

    if girl > first:
        break

    girl += 1
    first -= 1
    count += 1

    heapq.heappush(heap, -first)

print(count)