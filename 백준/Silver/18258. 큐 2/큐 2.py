"""

출력 입력할 빈 deque 선언
리스트 컴프리헨션으로 테스트 케이스 T만큼 commands 리스트에 채우기

함수 6개 선언
삼항연산자 연습
딕셔너리로 명령어 6개 저장

반복문 range는 T
만약 commands[i]가 push로 시작하면
commands[i]를 공백으로 split하고 언패킹 하고
두번째 항목을 int형으로 변환해서 push 함수를 실행

그 외에는 딕셔너리에서 commands[i]의 문자열과 일치하는 함수를 실행하는데
딱히 인자가 필요 없으니 인자는 비워서 ()으로 만든다
"""

import sys
from collections import deque

T = int(sys.stdin.readline().strip())
result = deque()
commands = [sys.stdin.readline().strip() for _ in range(T)]

def push(x):
    result.append(x)
def pop():
    print(result.popleft() if result else -1)
def size():
    print(len(result))
def empty():
    print(1 if not result else 0)
def front():
    print(result[0] if result else -1)
def back():
    print(result[-1] if result else -1)

command_dict = {
    "push": push,
    "pop": pop,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back
}

for i in range(T):
    if commands[i].startswith('push'):
        nothing, x = commands[i].split()
        push(int(x))
    else:
        command_dict[commands[i]]()