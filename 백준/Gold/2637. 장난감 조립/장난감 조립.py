"""
첫째 줄 N
1~N-1 -> 기본 부품 or 중간 부품의 번호

둘째 줄
부품 관계 개수 M

다음 M개의 줄
X,Y,K
중간 부품 또는 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다.
하나의 완제품을 조립하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력하되(중간 부품은 출력하지 않음)
반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록 한다.

기본에서 중간으로, 중간에서 완제품으로 가야 하니 방향이 정해진 acycilic 그래프가 맞긴 한데...
그럼 진입차수가 0인 것은 기본 부품들인가?

일단 빈 그래프 목록을 N+1개(1-based으로 하기 위해) 생성
그리고 진입차수를 0으로 모두 초기화. 이거도 당연히 N+1


"""

from collections import deque
import sys
input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
M = int(data[1])

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
needs = [[0] * (N + 1) for _ in range(N + 1)]

for line in data[2:]:
    x, y, k = map(int, line.split())    #X를 만드는데 Y가 K개 필요하다.
    graph[y].append((x, k)) # 부품 y를 써서 부품 x를 만들 수 있고 y는 k개 필요함 .
    in_degree[x] += 1   # 진입차수를 1씩 증가

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:   # 진입차수가 0인 것들을 pop
        queue.append(i) 
        needs[i][i] = 1 #   [i][i]인 형태인 경우 1로 초기화

while queue:    # quere가 빌 때까지
    now = queue.popleft()   #   queue에서 팝해서 now에 넣음

    for next_part, count in graph[now]: #pop한 것에 해당하는 graph의 next_part, count를 반복 인자로 받음
        for i in range(1, N + 1):
            needs[next_part][i] += needs[now][i] * count
            # now-> 현재 조립 중인 재료 부품 번호
            # next=_part : now를 이용해 만들 수 있는 결과 부품 번호
            # count : now가 몇 개 필요한지
            # i: 기본 부품 번호
            # 지금 조립 중인 now 부품을 count개 써서 next_part를 만든다 할 때
            # 그 now 부품이 만들기 위해 필요했던 기본 부품 i가 있다면
            # 그 i를 count배만큼 더해줘야 next_part가 요구하는 기본 부품 수를 정확히 누적할 수 있다.

        in_degree[next_part] -= 1   # next_part의 진입차수를 1 줄인다.
        if in_degree[next_part] == 0:   # next_part의 진입차수가 0이면
            queue.append(next_part) # queue에서 pop

for i in range(1, N + 1):
    if needs[N][i] > 0 and in_degree[i] == 0:
        print(i, needs[N][i])