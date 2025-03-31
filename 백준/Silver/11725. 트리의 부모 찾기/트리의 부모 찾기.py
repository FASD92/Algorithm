"""
루트가 없음
근데 루트를 1로 한다?
방향은 안 나와있으니 양방향?

일단 반복문으로 인접 리스트로 만듦
1 :6,4
2 : 4
3: 6,5
4: 1,2,7
5: 3
6: 1,3
7:4

그리고 1부터 돌림
(1,6)이니까 6의 부모는 1
그리고 6번 노드로 감
1번은 '루트를 1로 한다'라고 했으니 패스하고 (6,3)으로 감
3번의 부모는 6으로 설정
그리고 다시 (1,4)로 돌아옴

이런 식으로 쭉쭉 이어나감
대신 true/false 느낌으로 한번 간 곳을 체크하는 기능은 있어야 함 -> visited

그리고 결국 부모를 출력해야 하니까 부모를 저장하는 리스트도 있어야 함 -> parent
"""
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            dfs(neighbor)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])