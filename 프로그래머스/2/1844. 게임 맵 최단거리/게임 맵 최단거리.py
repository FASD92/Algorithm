"""
좌표가 있어야 할 것 같은데 이 좌표를 어떻게 만들지?
주어진 건 2차원 배열인데...
(1,1) = map[0][0] 이런 식으로 만들어져야 뭘 할 수 있는 것 아닌가?
인접행렬 없이 BFS로 뭘 할 수 있는 거지?

일단 (1,1) 기준 동서남북으로 갈 수 있는 후보를 찾아야 한다
하지만 행이 1일 때는 -1, n일 때는 +1을 할 수 없고
똑같이 열이 1일 때는 -1, n일 떄는 +1을 할 수 없다. <- 맵 이탈 방지 조건

그리고 maps[i][j] != 0 인 조건이어야 한다. 왜냐면 벽을 0으로 표현했기 때문.

"""
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    queue = deque([(0, 0, 1)])
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        y, x, dist = queue.popleft()
        
        if y == n - 1 and x == m - 1:
            return dist
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx, dist + 1))
    return -1