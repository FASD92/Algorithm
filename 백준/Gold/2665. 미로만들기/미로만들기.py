"""
0은 검은 방
1은 흰 방

그냥 1에서 0을 밟을 때마다 카운트 하면 되는 거 아닌가?

nxn 배열을 만드는데... 좌표 튜플을 키로, 값은 주어진 0 또는 1 -> maze

BFS -> 큐
(1,1)시작이니 큐에 (0,0)추가하고 시작
visited에도 (0,0)추가함

dx dy 테크닉 사용
-벽 체크
-밟은 곳은 visited 체크 -> 키는 튜플, 좌표는 현재까지 벽을 깬 횟수를 저장함.

while 문은 current_step이 (N-1,N-1)이 될 때까지?
아니면 queue가 완전히 빌 때까지? queue가 완전히 비었다는 것은 곧 N-1, N-1에 도착한 게 아닌가?

queue에서 팝 후에 current_step의 인접 좌표인 next_step을 체크함
이 때 next_step의 color가 0이면 벽을 부순 횟수인 count를 +=1 함
그리고 visitied에 추가함
그리고 큐에 추가함

이미 방문한 곳이라도 더 적은 벽을 부수고 도달했으면 다시 큐에 넣어서 탐색해야함


1에서 0을 밟은 걸 어떻게 체크하지"
"""
import heapq

N = int(input())
maze = {}
for i in range(N):
    line = input().strip()
    for j in range(N):
        maze[(i, j)] = int(line[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = {}
queue = []
heapq.heappush(queue, (0, 0, 0))
visited[(0, 0)] = 0

while queue:
    broken, x, y = heapq.heappop(queue)

    if (x, y) == (N - 1, N - 1):
        print(broken)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if maze[(nx, ny)] == 1:
                wall = 0
            else:
                wall = 1
                 
            total_walls_broken = broken + wall

            if ((nx, ny) not in visited) or (visited[(nx, ny)] > total_walls_broken):
                visited[(nx, ny)] = total_walls_broken
                heapq.heappush(queue, (total_walls_broken, nx, ny))
