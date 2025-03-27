"""
현재 queue의 가장 앞에 있는 문서의 중요도를 확인
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
이 문서를 인쇄하지 않고 queue의 가장 뒤에 재배치 한다.
그렇지 않다면 바로 인쇄한다.

최대힙을 써야 하나?

첫번째 줄 테스트 케이스 개수 T

두번째 줄에는
문서 개수 N, 찾아야 할 문서의 인덱스를 저장한 target이니까 언패킹해서 저장하고...
문서들의 우선순위를 리스트로 저장할 priorities

문서들의 우선순위와 인덱스를 함께 튜플로 저장한 리스트 documents를 deque로 만들고
-> [(우선순위, 인덱스)]
-> 인덱스는 0부터 시작

문서 개수 N만큼 documents에 위에서 말한 구조로 튜플로 저장함

출력한 문서(documents에서 pop된)를 차례대로 저장할 리스트 printed를 선언

만약 documents[0]이 우선순위가 가장 높지 않다면 -> 아마 max 쓰면 될 듯?
documents[0]을 popleft후 다시 append함

그게 아니라면 => 즉,documents[0]이 우선순위가 가장 높다면
documents[0]을 popleft하고 그걸 printed.append 함
그리고 printed[-1][1]이 target과 같다면(방금 출력한 문서의 인덱스가 우리가 찾아야 할 목표 인덱스와 같다면)
바로 print(len(printed))로 몇번째 인쇄됐는지 출력하고 while을 끝냄
"""
from collections import deque

T = int(input())

for _ in range(T):
    N, target = map(int, input().split())
    priorities = list(map(int, input().split()))
    documents = deque()

    for idx in range(N):
        documents.append((priorities[idx], idx))
    printed = []

    while documents:
        if documents[0][0] < max(doc[0] for doc in documents):
            documents.append(documents.popleft())
        else:
            printed.append(documents.popleft())
            if printed[-1][1] == target:
                print(len(printed))
                break