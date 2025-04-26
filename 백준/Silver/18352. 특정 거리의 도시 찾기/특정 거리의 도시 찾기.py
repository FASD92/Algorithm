"""
BFS
도시 개수 N
도로 개수 M
최단 거리 정보 K
출발 도시 X

입력 -> A B A번 도시에서 B번 도시로 간선이 존재

1. 노드는 도시, 간선은 도로
2. queue와 방문 표시용 배열 또는 딕셔너리 만들기
3. BFS 템플릿
while queue:
    현재 = queue.popleft()
    for 다음 in 현재 갈 수 있는 곳:
       if 아직 방문 안 함:
            방문 표시(이번 문제는 다음 도시로 갈 때마다 distance가 간선만큼(1만큼)추가되는 방식)
            큐에 추가


최단 거리 K인 도시를 못 찾을 때를 대비해서 check 변수를 미리 만들고

반복문 1부터 N+1까지
만약 distance, 즉 최단 거리가 K인 원소를 찾으면 print(i)를 하면서 check를 1로 초기화

만약 check가 0, 즉 위 반복문을 못 빠져나왔음에도 최단 거리를 못 찾으면 print(-1)

"""
import sys
from collections import deque

N, M, K, X = list(map(int, sys.stdin.readline().split()))

graph = []
for _ in range(N+1):
    graph.append([])

for _ in range(M):
    A, B = list(map(int, sys.stdin.readline().split()))
    graph[A].append(B)

distance = [-1] * (N+1)
distance[X] = 0

queue = deque()
queue.append(X)

#print(queue)
#print(visited)
#print(graph)

while queue:
    current = queue.popleft()

    for neigbor in graph[current]:
        if distance[neigbor] == -1:
            distance[neigbor] = distance[current] + 1
            queue.append(neigbor)
    
check = 0

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = 1

if check == 0:
    print(-1)
