"""
컴퓨터의 수 N
직접 연결되어 있는 컴퓨터 쌍의 수 M
양방향

infected -> set()?
근데 1이 감염의 시초니까
set(1)?

일단 두 노드의 쌍을 의미하는 입력을 튜플로 받음
그리고 해당 튜플의 [0]이 dict에 없으면 key를 dict에 추가한다.
해당 튜플의 [0]이 dict에 있으면 해당 튜플에 해당하는 key에 [1]을 값으로 추가한다.
이런 식으로 연결 리스트를 생성함

(1,2), (2,3), (1,5),(5,2), (5,6), (4,7)
이런 식으로 튜플이 생성될텐데 각 튜플마다 for문을 돌면서 1번과 연결된 노드들을 하나씩 check하고,
또 2번과 연결된 노드들(1,3)을 체크하고... 이런 식으로 모든 노드들을 다 check 함
check만 하면 안 되니까 당연히 infected라는 리스트에 추가함

근데 예를 들어 2번 노드 같은 경우 쌍은 1,3임.
그러면 무한 사이클이 돼버리니 해당 노드를 탐험할 때마다 infected에 추가함
그래서 infected에 추가된 노드는 다시 돌지 않고 반환함
근데 이렇게 되면 초기에 infected를 튜플의 개수 M개만큼 초기화 시켜야 하나?
"""
N = int(input())
M = int(input())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

infected = set()

def dfs(node):
    infected.add(node)
    for neighbor in graph[node]:
        if neighbor not in infected:
            dfs(neighbor)

dfs(1)
print(len(infected) - 1)