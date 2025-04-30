"""
1단계
노드 (N,M) 좌표
간선 dx dy 테크닉

dx, dy 테크닉 // 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

2단계
queue.deque -> (N,M) 좌표를 넣고 뺌
visited -> False로 2차원 처리
maze도 있어야 할 거 같은데... 얘는 append로 1, 0 즉 미로 만들기

3단계
while queue:
    x, y = queue.popleft()
        
        for i in range(4)
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maze[nx][ny]==1:
                    visited [nx][ny] = True
                    maze[nx][ny] = maze[x][y]+1
                    queue.append((nx,ny))
"""
import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))

visited = [([False] * M) for _ in range(N)]

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

#print(maze)
#print(visited)

# dx dy 테크닉 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

print(maze[N-1][M-1])