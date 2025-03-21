"""
카드 개수 N -> int
카드 배열을 저장하는 cards를 deque로 선언
deque 선언할 때 입력은 1보다 크거나 같은 정수니까 1-based로 만든다.

함수명은 shuffle, 인자는 cards를 받음
만약 len(cards)==1, 'cards[0]' => base case임
아니면
popleft() 한번 한다
그리고 if문을 빠져나오면서 popleft()한번 더 한 것을 append해서 다시 cards에 추가한다. 윗줄에서 popleft()한 거랑은 또 다른 popleft()다!
밑줄에는 마지막으로 return shuffle(cards)로 재귀함수를 호출하면서 함수를 끝낸다

그리고 shuffle(cards)함수의 반환값을 print 출력한다.

from collections import deque
N = int(input())
cards = deque(range(1,N+1))

def shuffle(cards):
    if len(cards) == 1:
        return cards[0]
    else:
        cards.popleft()
    cards.append(cards.popleft())
    return shuffle(cards)

print(shuffle(cards))

그래서 이렇게 풀어서 예제는 맞았는데 recursion error가 백준에서 떴음
"""
from collections import deque

N = int(input())
cards = deque(range(1, N+1))

while len(cards) > 1:
    cards.popleft()           # 제일 위 카드 버림
    cards.append(cards.popleft())  # 다음 카드를 맨 뒤로

print(cards[0])