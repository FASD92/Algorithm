"""
1. NxN
2. (0,0) 시작
3. 이동 가능 방향은 오른쪽과 아래 뿐
4. (N,N)
5. 칸 이동 숫자가 적혀 있는 2차원 배열...
6. (N,N)에는 -1이 있음
7. 칸에 적힌 '숫자만큼만' 이동할 수 있음
"""

import sys
from collections import deque

data = sys.stdin.read().split()
n = int(data[0])

visited = [[False] * n for _ in range(n)]
queue = deque()
queue.append((0, 0))
visited[0][0] = True

def dfs():
    grid = []
    idx = 1
    for _ in range(n):
        row = list(map(int, data[idx:idx+n]))
        grid.append(row)
        idx += n
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == n-1:
            print("HaruHaru")
            return
        
        jump = grid[x][y]
        
        if y + jump < n and not visited[x][y + jump]:
            visited[x][y + jump] = True
            queue.append((x, y + jump))
        
        if x + jump < n and not visited[x + jump][y]:
            visited[x + jump][y] = True
            queue.append((x + jump, y))
    
    print("Hing")

dfs()