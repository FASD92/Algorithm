"""
안전 영역 DFS로 풀 때랑 비슷한 듯?
관건은 단지의 개수, 단지에 속하는 집의 수를 어떻게 셀지였음

단지에 속하는 집의 수는 count 변수를 재귀로 넘겼고
단지의 개수는 조건에 맞는, 즉 dfs를 실행하고 그 반환값을 result라는 리스트에 append 했음
그리고 그 리스트의 길이를 구해서 그걸 단지의 개수로 출력했다
단지에 속한 집의 개수들은 result 리스트에 저장된 count 원소들을 오름차순으로 출력
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

houses = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]* N for _ in range(N)]
result = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
        visited[x][y] = True
        count = 1

        for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and houses[nx][ny] == 1:
                                count += dfs(nx, ny)
        return count

for i in range(N):
        for j in range(N):
                if houses[i][j] == 1 and not visited[i][j]:
                        result.append(dfs(i, j))
print(len(result))
for i in sorted(result):
        print(i)