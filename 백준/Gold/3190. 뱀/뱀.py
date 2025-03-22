from collections import deque
import sys

input = sys.stdin.readline
N = int(input().strip())
K = int(input().strip())

apples = []
for _ in range(K):
    x, y = map(int, input().strip().split())
    apples.append((x, y))

L = int(input().strip())
turns = []
for _ in range(L):
    x, c = input().strip().split()
    turns.append((int(x), c))

worm = deque([(1, 1)])
second = 0

def up(head):
    return (head[0] - 1, head[1])

def down(head):
    return (head[0] + 1, head[1])

def left(head):
    return (head[0], head[1] - 1)

def right(head):
    return (head[0], head[1] + 1)

turn = {
    'R': {'L': 'U', 'D': 'D'},
    'D': {'L': 'R', 'D': 'L'},
    'L': {'L': 'D', 'D': 'U'},
    'U': {'L': 'L', 'D': 'R'}
}

movement = {
    'R': right,
    'L': left,
    'U': up,
    'D': down
}

current_direction = 'R'
head = worm[-1]
turn_idx = 0

while True:
    second += 1

    if turn_idx < L:
        next_turn_time, next_turn_dir = turns[turn_idx]

    new_head = movement[current_direction](head)

    if (new_head[0] < 1 or new_head[0] > N or 
        new_head[1] < 1 or new_head[1] > N or 
        new_head in worm):
        print(second)
        break

    worm.append(new_head)

    if new_head in apples:
        apples.remove(new_head)
    else:
        worm.popleft()

    head = new_head

    if second == next_turn_time:
        current_direction = turn[current_direction][next_turn_dir]
        turn_idx += 1