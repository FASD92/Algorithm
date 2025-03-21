"""
딕셔너리로 명령어 6개 저장
"""

import sys
from collections import deque

T = int(sys.stdin.readline().strip())
result = deque()
commands = [sys.stdin.readline().strip() for i in range(T)]

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