"""
1번부터 N번까지 번호가 매겨져 있는 도시들
도시들 사이에는 길이 있을 수도 없을 수도 있음
N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로
한 번 갔던 도시로는 다시 갈 수 없음
가장 적은 비용이 드는 여행 계획

각 도시간 이동 비용은 행렬 W[i][j]
W[i][j]는 도시 i에서 도시 j로 가는 데 드는 비용
비용은 대칭적이지 않음
도시 i에서 도시 j로 갈 수 없는 경우, W[i][j] = 0

각 행렬의 성분은 1,000,000 이하의 양의 정수

dfs로 풀 수 있지만... 기존 dfs 3단계로는 풀 수가 없음
일단 min_cost를 충분히 큰 값으로 초기화해야 하는데
이는 가장 비용이 적게 드는 걸 찾기 위함임

그리고 마지막 도시에 도착해도 시작 도시로 돌아올 수 없다면
그 case는 실패기 때문에 그에 대한 처리도 해줘야 함 -> 백트래킹

"""
import sys

N = int(sys.stdin.readline().strip())
W = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

min_cost = 10 ** 9

def dfs(start, current, count, cost, visited):
    global min_cost

    if cost >= min_cost:  # 가지치기
        return

    if count == N:
        if W[current][start] != 0:
            min_cost = min(min_cost, cost + W[current][start])
        return

    for next in range(N):
        if not visited[next] and W[current][next] != 0:
            visited[next] = True
            dfs(start, next, count + 1, cost + W[current][next], visited)
            visited[next] = False

for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i, i, 1, 0, visited)

print(min_cost)