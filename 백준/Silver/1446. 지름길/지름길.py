"""
지름길의 개수 N
고속도로의 길이 D

지름길의 정보가 담기는 배열 shortcuts = []
이 때 shortcuts에는 지름길의 끝이 고속도로의 길이보다 작은 경우만 저장됨



"""
import sys
import heapq

input = sys.stdin.readline
N, D = map(int, input().split())
shortcuts = []

for _ in range(N):
    start, end, cost = map(int, input().split())
    if end <= D:
        shortcuts.append((start, end, cost))

#print(shortcuts)

# 위치 i까지 가는 최소 거리를 나타내는 distance
# 시작 지점 0의 거리는 0
distance = [float('inf')] * (D + 1)
distance[0] = 0

#(거리,위치) 형식으로 저장 -> 거리 기준으로 최소값 우선 정렬됨
# 시작 위치 0에서 시작, 현재까지 거리도 0
heap = [(0,0)]

while heap:
    total_dist, cur_pos = heapq.heappop(heap) # 현재 거리 cur_dist, 현재 위치 cur_pos

    if cur_pos > D: # 목적지를 넘어간 지름길이 있을 경우 무시
        continue

    if distance[cur_pos] < total_dist:    # 이미 더 짧은 거리로 cur_pos에 도달한 적 있으면 continue
        continue

    # 기본 도로 이동 : 현재 위치에서 한 칸 앞으로 이동(비용 1)
    if cur_pos + 1 <= D and distance[cur_pos + 1] > total_dist + 1:
        distance[cur_pos + 1] = total_dist + 1
        heapq.heappush(heap, (distance[cur_pos + 1], cur_pos + 1))  # 만약 새로운 비용이 기존보다 작으면 큐에 삽입

    for start, end, short in shortcuts:
        if start == cur_pos and distance[end] > total_dist + short:   # 현재 위치에서 출발하는 지름길인지 확인하고,
                distance[end] = total_dist + short  # 지금까지의 누적 거리 + 지름길 비용이 기존에 거리보다 짧다면 갱신
                heapq.heappush(heap, (distance[end], end))

print(distance[D])