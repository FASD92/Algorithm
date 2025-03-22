"""
보드 크기 N
사과 개수 K

다음 K개의 줄에서 사과의 좌표를 입력받아 튜플로 저장
apples 리스트에 좌표들 저장
방향 전환 횟수 L 입력

다음 L개의 줄에서 방향 전환 정보를 입력
각 줄은 (X초, C방향) 형태이며 리스트 turns에 저장

뱀의 위치를 저장할 worm은 deque로 선언
시작 위치는 (1, 1)

head는 worm의 마지막 요소 (뱀 머리 위치)
second는 시간 측정용 변수로, 0으로 초기화

4개의 방향 함수 정의
up, down, left, right
각 함수는 현재 좌표를 받아 다음 좌표를 반환

현재 방향에 따라 다음 방향을 결정하는 turn 딕셔너리 정의
예: 'R' 상태에서 'L' => 'U'

각 방향 문자열에 해당하는 이동 함수 mapping을 movement 딕셔너리에 저장
예: 'U'는 up 함수

current_direction은 현재 뱀의 이동 방향으로 'R'로 초기화

turn_idx는 초와 방향 변환 정보가 담긴 turns 리스트에서 다음 방향 전환 정보를 참조하기 위한 인덱스

무한 반복 시작
1초가 지남 → second += 1
turn_idx가 L보다 작으면 => 다음 방향 전환 정보가 남아있는지를 확인
다음 방향 전환 시각과 방향 정보를 언패킹해서 next_turn_time, next_turn_dir로 저장

현재 방향(current_direction)에 따라 새로운 머리 좌표 new_head 계산
만약 new_head가 보드 범위를 벗어나거나 worm 내부에 이미 있다면 second 출력 후 프로그램 종료

worm에 new_head를 추가
new_head 위치에 사과가 있다면 apples에서 해당 좌표 제거
없다면 worm의 꼬리 제거 (몸길이 유지) 그리고 head를 new_head로 갱신

만약 second가 next_turn_time과 같다면:
current_direction을 방향 전환 딕셔너리를 통해 갱신
turn_idx += 1

근데 나는 왜 자꾸 지렁이가 생각날까
문제는 뱀인데
"""



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

# 각 방향에 맞는 함수들 생성
def up(head):
    return (head[0] - 1, head[1])

def down(head):
    return (head[0] + 1, head[1])

def left(head):
    return (head[0], head[1] - 1)

def right(head):
    return (head[0], head[1] + 1)

# 오른쪽으로 가던 중 L이 입력되면 up, D가 입력되면 down 이런 식으로 딕셔너리 생성
turn = {
    'R': {'L': 'U', 'D': 'D'},
    'D': {'L': 'R', 'D': 'L'},
    'L': {'L': 'D', 'D': 'U'},
    'U': {'L': 'L', 'D': 'R'}
}

# 방향을 키, 방향 함수를 값으로 한 딕셔너리 생성
movement = {
    'R': right,
    'L': left,
    'U': up,
    'D': down
}

current_direction = 'R'
head = worm[-1]
turn_idx = 0

while True: #   무한히
    second += 1 #   일단 1초 증가

    if turn_idx < L:    # 방향 전환 정보가 남아있는지 여부 체크
        next_turn_time, next_turn_dir = turns[turn_idx] # 해당 정보 언패킹해서 방향 전환 시간과, 방향 정보 저장

    new_head = movement[current_direction](head)    #   현재 방향

    if (new_head[0] < 1 or new_head[0] > N or   # 뱀의 머리가 y축, 즉 열을 벗어났거나
        new_head[1] < 1 or new_head[1] > N or   # 뱀의 머리가 x축, 즉 행을 벗어났거나
        new_head in worm):  # 뱀의 머리 좌표가 worm 리스트 안에도 있을 때, 즉 머리가 본인 몸에 부딪혔을 때
        print(second)   # 해당 초를 출력하고
        break   # 종료

    worm.append(new_head)   # 머리 추가

    if new_head in apples:  # 추가한 머리에 위치한 좌표가 사과의 좌표가 담긴 apples에 있는지 조회하고
        apples.remove(new_head) # 해당 좌표에 해당하는 사과를 apples에서 제거
    else:
        worm.popleft()  # 그게 아니면, 즉 머리가 사과에 닿지 않았으면 벌레 꼬리 제거

    head = new_head # 머리 좌표를 업뎃

    if second == next_turn_time:    # 만약 지금 초가 '방향이 바뀌는 초와 일치하면'
        current_direction = turn[current_direction][next_turn_dir]  # 현재 방향을 입력된 방향으로 바꾸고
        turn_idx += 1   #   다음 방향 정보 인덱스로 넘어간다